from collections import defaultdict
k_clusters = [250,240,260,210,100,75]
time = [21,22,23,0,1,2]
all_data = pickle.load(open("all_data.p", "rb"))
for k,t in zip(k_clusters,time):
    lat_long = [row[2:] for row in all_data[t]]
    kmeans = km(k,max_iter=1000,n_init=50,init='k-means++')
    kmeans.fit(lat_long)
    density = defaultdict(int)
    for i in kmeans.labels_: 
        density[i] += 1
    f = open('clusters_{t_val}_{k_val}.txt'.format(t_val = t, k_val = k),'w')
    f.write("lat,long,density\n")
    for i,centroid in enumerate(kmeans.cluster_centers_.tolist()):
        c = "{lat_val},{long_val},{density_val}\n".format(lat_val=centroid[0], long_val=centroid[1],density_val=density[i])
        f.write(c)
    f.close()
