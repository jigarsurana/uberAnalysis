import cPickle as pickle
import matplotlib.pyplot as plt
from collections import defaultdict
import plotly.plotly as py
import plotly.graph_objs as go

all_data_original = pickle.load(open("../data/all_data_original.p", "rb"))

# 4/20/2014 - Sunday,  5/26/2014 - Monday,  7/4/2014 - Friday,  9/1/2014 - Monday
holiday_list = set(["4/20/2014", "5/26/2014", "7/4/2014", "9/1/2014"])

holidays = defaultdict(list)
otherdays = defaultdict(list)

for time, lists in all_data_original.items():
    for row in lists:
        crap = [row[1], row[2].split(":")[0], float(row[3]), float(row[4])]
        if row[1] in holiday_list:
            holidays[row[0]].append(crap)
        else:
            otherdays[row[0]].append(crap)

holiday = holidays["Friday"]
otherday = otherdays["Friday"]

x, y = [], []
times = defaultdict(int)
for row in holiday:
    times[int(row[1])] += 1
for i in range(len(times)):
    x.append(i)
    y.append(times[i] / 1)

x_, y_ = [], []
times_ = defaultdict(int)
for row in otherday:
    times_[int(row[1])] += 1
for i in range(len(times_)):
    x_.append(i)
    y_.append(times_[i] / 25)


hours = ["00:00", "1:00","2:00","3:00","4:00","5:00","6:00","7:00","8:00","9:00","10:00","11:00",\
         "12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00","22:00",\
         "23:00"]

trace0 = go.Scatter(
    x = hours,
    y = y,
    name = 'Holiday-Sunday',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4)
)

trace1 = go.Scatter(
    x = hours,
    y = y_,
    name = 'Non-Holiday-Sunday',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4)
)


layout = dict(title = 'Cab frequencies in New York',
              xaxis = dict(title = 'Hours'),
              yaxis = dict(title = 'Frequency')
              )

data = [trace0, trace1]

fig = dict(data=data, layout=layout)
py.iplot(fig, filename='styled-line')
