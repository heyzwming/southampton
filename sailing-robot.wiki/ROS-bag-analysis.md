# Using rosbag_pandas
```
import rosbag_pandas
%matplotlib qt4
df = rosbag_pandas.bag_to_dataframe('file.bag')
list(df)
df.something_you_want_to_plot.dropna().plot()
```