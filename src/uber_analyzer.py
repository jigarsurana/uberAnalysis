import csv
import numpy as np
import datetime
from sklearn.cluster import KMeans as km
import cPickle as pickle
from collections import defaultdict

all_data_new = defaultdict(list)
all_data = defaultdict(list)

time_nset = set(['21','22','23'])
time_dset = set(['0','1','2'])
time_set = set(['21','22','23','0','1','2'])
l_files = ['../data/uber-raw-data-apr14.csv', '../data/uber-raw-data-may14.csv', '../data/uber-raw-data-jun14.csv', '../data/uber-raw-data-jul14.csv', '../data/uber-raw-data-aug14.csv', '../data/uber-raw-data-sep14.csv',]
for filename in l_files:
	with open(filename, 'rb') as f:
		reader = csv.reader(f)
		i = 0
		for row in reader:
			if i == 0:
				i += 1
				continue
			t = row[0].split()[1].split(':')[0]
			d = row[0].split()[0]
			month, day, year = (int(x) for x in d.split('/'))
			ans = datetime.date(year, month, day)
			weekday = ans.strftime("%A")
			row = [weekday, row[0].split()[0], row[0].split()[1], float(row[1]), float(row[2])]
			if (t in time_nset and weekday == 'Friday') or (t in time_set and weekday == 'Saturday') or (t in time_dset and weekday == 'Sunday'):
				all_data[int(t)].append(row)
				if row[3] >= 40.61 and row[3] <= 40.91 and row[4] >= -74.06 and row[4] <= -73.77:
					all_data_new[int(t)].append(row)

pickle.dump(all_data_new, open("all_data_new.p", "wb"))

# kmeans = km(10000, init='k-means++', n_jobs = -2)
# kmeans.fit(x)

