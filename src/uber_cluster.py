import cPickle as pickle
from sklearn.cluster import KMeans as km

all_data = pickle.load(open("all_data.p", "rb"))

t = 22
lat_long = []
for row in all_data[t]:
	lat_long.append([row[2], row[3]])

for k in [240]:
	kmeans = km(k, max_iter=1000, n_init = 50,init = 'k-means++')
	kmeans.fit(lat_long)
	f = open('output_{t_val}_{k_val}.txt'.format(t_val = t, k_val = k),'w')
	s = "k = {k_val}, inertia = {inertia_}\n".format(k_val = k, inertia_ = kmeans.inertia_)
	f.write(s)
	f.close()