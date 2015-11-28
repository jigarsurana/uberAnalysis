import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np

t = 1
k = range(100,205,5)
l_files = ['../outputs/output_{t_val}_{k_val}.txt'.format(t_val=t,k_val=i) for i in k]

mse = []

for filename in l_files:
	with open(filename, 'rb') as f:
		s = f.read()
		mse.append(float(s.split()[-1]))

plt.clf()
plt.plot(k,mse,'-')
plt.xlabel('cluster size K')
plt.grid(True)
plt.ylabel('MSE')
plt.show()
