import cPickle as pickle
from sklearn.cluster import KMeans as km
from geopy.distance import vincenty

lyft = pickle.load(open("../data/all_data_lyft.p", "rb"))

t = 23
lyft_lat_long = []
for row in lyft[t]:
	lyft_lat_long.append([row[3], row[4]])

pred = kmeans.predict(lyft_lat_long)

pred_cluster_centers = [kmeans.cluster_centers_[i] for i in pred]

error = [vincenty(lyft_lat_long[i],pred_cluster_centers[i]).miles for i in range(len(lyft_lat_long))]

print "For t = {t_val}:".format(t_val = t)
print "Min Error\t\tMax Error\tAvg Error".format()
print "{min_e}\t{max_e}\t{avg_e}".format(min_e = min(error), max_e = max(error), avg_e = sum(error)/len(error))