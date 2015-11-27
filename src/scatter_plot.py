import matplotlib.pyplot as plt
from collections import defaultdict
lat = kmeans.cluster_centers_[:,0]
longitude = kmeans.cluster_centers_[:,1]
density = defaultdict(int)
for i in kmeans.labels_: 
    density[i] += 1
max_density = max(density.values())
new_density = [float(density[i])/max_density for i in density]    
colors = np.random.rand(len(lat))
area = np.pi * (15 *  np.array(new_density))**2
plt.clf()
plt.cla()
plt.scatter(lat, longitude, s=area, c=colors, alpha=0.5)
plt.show()
