import csv
import numpy as np
import datetime
from sklearn.cluster import KMeans as km
from sklearn.cluster import MiniBatchKMeans as mkm
from sklearn import metrics
import cPickle as pickle

all_data = []
time_nset = set(['21','22','23'])
time_dset = set(['0','1','2'])
time_set = set(['21','22','23','0','1','2'])
l_files = ['uber-raw-data-apr14.csv', 'uber-raw-data-may14.csv', 'uber-raw-data-jun14.csv', 'uber-raw-data-jul14.csv', 'uber-raw-data-aug14.csv', 'uber-raw-data-sep14.csv',]
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
			if (t in time_nset and weekday == 'Friday') or (t in time_set and weekday == 'Saturday') or (t in time_set and weekday == 'Sunday') or (t in time_dset and weekday == 'Monday'):
				all_data.append(row)

pickle.dump(all_data, open( "all_data.p", "wb" ) )

x = np.array(lat_long[:100000])

# mkmeans = mkm(10000, max_iter=300, batch_size=10000, init='k-means++')
# mkmeans.fit(x)

# kmeans = km(10000, init='k-means++', n_jobs = -2)
# kmeans.fit(x)

