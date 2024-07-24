from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt 
import numpy as np 
from pylab import *
import matplotlib.cm as cm
import pandas as pd
results_folder = "Oven_output"
data = np.genfromtxt("oven_output.txt", delimiter=" ")
t_res = data[:,0] #days
temp = data[:,1] #deg C
t_oven = data[:,2]
N = data[:,3]
data = {t_oven,temp, t_res, N}
df = pd.DataFrame(data)
heatmap_data = df.pivot(index=temp, columns=t_res, values=N)
t_res_values = heatmap_data.columns.values
temp_values = heatmap_data.index.values
N_values = heatmap_data.values
plt.figure(figsize=(10, 6))
plt.imshow(N_values, cmap='viridis', interpolation='nearest', origin='lower')
plt.show()
