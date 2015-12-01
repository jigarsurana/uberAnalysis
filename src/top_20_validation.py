from geopy.distance import vincenty
import cPickle as pickle
from sklearn.cluster import KMeans as km

all_data = pickle.load(open("../data/all_data_new.p", "rb"))

with open('../data/top_20_yelp.txt', 'rb') as f:
	s = f.read()

lines = s.split('\n')
top_yelp = []
for line in lines:
	if line.strip() == "":
		break 
	name = line.split(':')[0].strip()
	location = line.split(':')[1].strip().split(',')
	top_yelp.append([name, float(location[0].strip()), float(location[1].strip())])

top_yelp_lat_long = []
for row in top_yelp:
	top_yelp_lat_long.append([row[1], row[2]])

t = 21
lat_long = []
for row in all_data[t]:
	lat_long.append([row[3], row[4]])

for k in [240]:
	kmeans = km(k, max_iter=1000, n_init = 50,init = 'k-means++')
	kmeans.fit(lat_long)


pred = kmeans.predict(top_yelp_lat_long)

pred_cluster_centers = [kmeans.cluster_centers_[i] for i in pred]

error = [vincenty(top_yelp_lat_long[i],pred_cluster_centers[i]).miles for i in range(len(top_yelp_lat_long))]

print "For t = {t_val}:".format(t_val = t)
print "Min Error\t\tMax Error\tAvg Error".format()
print "{min_e}\t{max_e}\t{avg_e}".format(min_e = min(error), max_e = max(error), avg_e = sum(error)/len(error))