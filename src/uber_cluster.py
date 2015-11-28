import cPickle as pickle
from sklearn.cluster import KMeans as km

all_data = pickle.load(open("../data/all_data_new.p", "rb"))

t = 21
lat_long = []
for row in all_data[t]:
	lat_long.append([row[3], row[4]])

for k in range(160,290,10):
	kmeans = km(k, max_iter=1000, n_init = 50,init = 'k-means++')
	kmeans.fit(lat_long)
	f = open('../outputs/output_{t_val}_{k_val}.txt'.format(t_val = t, k_val = k),'w')
	s = "k = {k_val}, inertia = {inertia_}\n".format(k_val = k, inertia_ = kmeans.inertia_)
	f.write(s)
	f.close()