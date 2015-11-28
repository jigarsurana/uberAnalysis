import cPickle as pickle
from sklearn.cluster import KMeans as km
from collections import defaultdict
import pandas as pd

all_data = pickle.load(open("../../all_data_original.p", "rb"))

t = 23
d = defaultdict(list)
for row in all_data[t]:
	d['latitude'].append(float(row[3]))
	d['longitude'].append(float(row[4]))

df = pd.DataFrame(data=d)

import matplotlib  
import matplotlib.pyplot as plt  

pd.options.display.mpl_style = 'default' #Better Styling  
new_style = {'grid': False} #Remove grid  
matplotlib.rc('axes', **new_style)
from matplotlib import rcParams  
rcParams['figure.figsize'] = (17.5, 17) #Size of figure  
rcParams['figure.dpi'] = 250

P=df.plot(kind='scatter', x='longitude', y='latitude',color='white',xlim=(-74.06,-73.77),ylim=(40.61, 40.91),s=.002,alpha=0.5)

P.set_axis_bgcolor('black') #Background Color