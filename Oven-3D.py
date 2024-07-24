# 3D Heatmap in Python using matplotlib 
  
# importing required libraries 
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt 
import numpy as np 
from pylab import *
import matplotlib.cm as cm
results_folder = "Oven_output"
data = np.genfromtxt("oven_output.txt", delimiter=" ")
t_res = data[:,0] #days
temp = data[:,1] #deg C
t_oven = data[:,2]
N = data[:,3]

# creating figures 
fig = plt.figure(figsize=(10, 10)) 
ax = fig.add_subplot(111, projection='3d') 
  
# setting color bar 
color_map = cm.ScalarMappable(cmap = 'jet') 
color_map.set_array(N) 
  
# creating the heatmap 
img = ax.scatter(t_res, temp, t_oven, 
                 s=200, c=N, marker = 's', cmap='jet') 
plt.colorbar(color_map) 
  
# adding title and labels 
ax.set_title("3D Heatmap") 
ax.set_xlabel('Residence time / days') 
ax.set_ylabel('Temperature / degrees Celsius') 
ax.set_zlabel('Baking time / s') 
  
# displaying plot 
plt.show() 