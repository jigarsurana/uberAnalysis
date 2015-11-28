import datetime
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go

all_data_original = pickle.load(open("all_data_original.p", "rb"))

b = {}
for h in range(0,24):
    print h
    d = defaultdict(list)
    for data in all_data_original[h]:
        print data[h]
        d[data[0]].append(data)
    b[h] = d

plot_matrix = [[0]*24 for _ in xrange(7)]
weekday_num = {'Monday':6,'Tuesday':5,'Wednesday':4,'Thursday':3,'Friday':2,'Saturday':1,'Sunday':0}
for h in range(24):
   for day in ['Monday', 'Tuesday', 'Friday', 'Wednesday', 'Thursday', 'Sunday', 'Saturday']:
    plot_matrix[weekday_num[day]][h] = len(b[h][day])/26

y_labels = ['Sun', 'Sat', 'Fri', 'Thu', 'Wed', 'Tue', 'Mon']
x_labels = range(24)

data = [
    go.Heatmap(
        z=plot_matrix,
        x=x_labels,
        y=y_labels,
        colorscale='Viridis',
    )
]

layout = go.Layout(
    title='Uber Rides Distribution',
    xaxis = dict(ticks='', nticks=36),
    yaxis = dict(ticks='' )
)

fig = go.Figure(data=data, layout=layout)

url = py.plot(fig, filename='datetime-heatmap1')