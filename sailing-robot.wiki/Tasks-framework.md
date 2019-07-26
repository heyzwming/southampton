The robot knows what to do via a sequence of *tasks*. Each task can calculate
what the boat should do given the current status, and whether the task
is complete. When a task says it is complete, the next task is started. If the
boat completes the last task, it will go back to the first one.

The most common task is to go to a waypoint. This will point the boat towards
the waypoint (or calculate tacking if it needs to go upwind). It is completed
when the boat reaches a circle of specified radius around the waypoint.

## Specifying tasks

Tasks are given as a list in the parameter file; typically we put them in a file
named `..._waypoints.yaml`. For instance:

```yaml
wp/tasks:
- {"kind": "to_waypoint", "waypoint": "4"}
- {"kind": "to_waypoint", "waypoint": "5"}
- {"kind": "keep_station", "waypoint": "5", linger: 60}
- {"kind": "to_waypoint", "waypoint": "6"}
```

Optional parameters for tasks may be specified in these dictionaries.

## Defining tasks in Python

Tasks inherit from `TaskBase` and define a few methods:

```python
from sailing_robot.taskbase import TaskBase

class StupidTask(TaskBase):
    def __init__(self, nav):
        self.nav = nav  # The nav object holds things like position and heading
        # This may also accept other parameters

    def start(self):
        '''Called when the task is started.'''
        pass

    def check_end_condition(self):
        '''Return True when this task is done.'''
        return True  # This would finish instantly

    def calculate_state_and_goal(self):
        '''Return the sailing state and goal heading.'''
        return 'normal', self.nav.heading  # This just carries on where it's going
```

The mapping from task names for parameter files to task classes is in
`sailing_robot.tasks`; I need to make this simpler.

## Tasks and ROS

The ROS node `tasks` runs tasks based on the parameters set.

The tasks framework and task classes don't rely on ROS, so they can be tested
without ROS installed. However, there is some integration with ROS features:

A task may call `self.log(level, msg)`, e.g. `self.log('warning', 'Here be monsters')`.
Outside ROS, the message is printed to stderr; within ROS it will use the
ROS logging facilities.

Tasks may define debug topics, which they can publish on while they are active.
These topics are defined by a list on the class, and published as
`self.debug_pub(topic, value)`. E.g.:

```python
class MyTask(TaskBase):
    debug_topics = [
      ('heading_to_waypoint', 'Float32'),
      ('distance_to_waypoint', 'Float32'),
    ]
    
    def calculate_state_and_goal(self):
        self.debug_pub('heading_to_waypoint', 270.0)
        ...
```

Outside of ROS, these debug topics are (for now) ignored.
