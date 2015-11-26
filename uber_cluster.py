import cPickle as pickle
from sklearn.cluster import KMeans as km

all_data = pickle.load(open("all_data.p", "rb"))

t = 21
lat_long = []
for row in all_data[t]:
	lat_long.append(row[2:])

for k in [500,1000,2000,3500,5000,6500,8000,10000,12500,15000]:
	kmeans = km(k, init='k-means++')
	kmeans.fit(lat_long)
	f = open('output_{t_val}_{k_val}.txt'.format(t_val = t, k_val = k),'w')
	s = "k = {k_val}, inertia = {inertia_}\n".format(k_val = k, inertia_ = kmeans.inertia_)
	f.write(s)
	f.close()
