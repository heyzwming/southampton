The helming node handles how a switch of tack is done. The associated code is [here](https://github.com/Maritime-Robotics-Student-Society/sailing-robot/blob/master/src/sailing_robot/scripts/helming).
The high level tells that a switch of tack is needed by changing the `sailing_state` topic from `normal` to `switch_to_stb_tack` or `switch_to_port_tack`. 

The helming node will then try to tack or jibe to complete the manoeuvre. Any kind of tack or jibe is called a "procedure". The helming node implements several different procedures from simple tack (rudder in full position) to more complex ones like going at 80 degree for a bit to build up speed before tacking. And it tries each of them in order until it succeeds to switch tack. The order in which the procedure are tested is dynamic and depends on previous attempts and the time they took.

# Parameters to set
3 parameters are associated with the helming node and the procedure system:
* `procedure/jibe_to_turn`, by setting this to true, the jibe will be the first procedure to be tested, and hence prioritised over the other. On the contrary setting it to false will try a simple tack first.
* `procedure/timeout`, a duration in second is expected. This is the time after which a procedure is considered failed and the next one is tried.
* `procedure/exploration_coefficient`: here a number between 0 and 1 is expected. The procedure handling is based on a fixed list of procedure, the first item on the list will be tried first. If it succeed once, it will remain the 1st to be tried next time. In order to find a better procedure that may be later in the list this coefficient gives the probability of trying an other procedure in the list (exploration). If it is set to 0, no exploration will be conducted and the list will always have the same order, if set to 1 at each new tack procedures that haven't been tested will be at the top of the list and tried 1st. A value of 0.3 means that in 30% of tacks the "best" procedure will not be used but an untested procedure will be tried first.



# Implementation

### Functions `set_sail` and `set_rudder`
These two functions are black boxes that publishes the appropriate messages to the hardware to set the sail at a particular position (either based on wind direction or at a specific position), or set the rudder at a particular angle.
These two functions have to be used directly, and only these functions should publish `rudder_control` and `sheet_normalized` messages.

### What is a Procedure?
A procedure is a `class` that will handle a way of switching tack. It inherit from the `ProcedureBase` class that handles the timing for example. A procedure needs at least an `__init__` function will call the `ProcedureBase` one with super, and a `loop` function.
The loop function is run at each time step, it shouldn't have any for/while loop in it nor any wait. It should call once the function `set_sail` and `set_rudder`. The `TackBasic` class is a good example of a minimal working procedure.

### Procedure handle
The class `ProcedureHandle` takes care of the priority in the procedure list. It is initialised with an ordered list of procedure. Before each switching of tack manoeuvre, the list of procedure `ProcedureList` is reordered based on weight, the procedure with the minimum weight starts etc. The weight is the average time the procedure took in the last 10 attempts. A fail attempt count as 1.5 times the timeout. A procedure that has not been tried yet doesn't have any weight, when the order is computed it gets a weight of either the timeout (+ a small delta) or a very small quantity (based on the `exploration_coefficient` parameter and a random pick).

Once tack manoeuvre is started the ProcedureList doesn't change any more, it gets reordered only at the next tack manoeuvre.

The `ProcedureHandle` class also publishes the topic `dbg_helming_procedure` with information about the current procedure tested and the success/failure outcome of it.

### Helming class
The helming class is the one handling the main loop (`while not rospy.is_shutdown()`) as well as calls to `_.loop()` from current the procedure in the list. It also defines the 2 orders of the `ProcedureList` (with `jibe_to_turn` set to true and to false).