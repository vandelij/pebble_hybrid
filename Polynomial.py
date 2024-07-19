import festim as F
my_model = F.Simulation()
import numpy as np
import sympy as sp
from festim import x,y,z,t
import fenics
import scipy.interpolate as interp
import matplotlib.pyplot as plt
import scipy.interpolate as interp

r_p = 3e-2
def arrmax(A):
    maxi = float('-inf')  # Initialize maxi as negative infinity
    for num in A:
        if num > maxi:
            maxi = num
    return maxi

# def remove_duplicates(arr1):
#     seen = set()
#     result1 = []
#     arr2 = []
#     for item in arr1:
#         if item not in seen:
#             seen.add(item)
#             result1.append(item)
#         else:
#             arr2.append((np.where(arr1==item)))
#     return result1, arr2

results_folder = "Cm measurements"
data = np.genfromtxt(results_folder + '/Flux.txt', skip_header=1, delimiter=",")
full = data[:,0]
p = arrmax(max(np.asarray(np.where(full < r_p))))
ovenxold = data[:p,0]
ovenyold = data[:p, len(data[0])-1]
ovenx = np.unique(ovenxold)

def find_missing_indices(arr1, arr2):
    missing_indices = []
    index = 0
    
    # Sort arr1 and arr2 (if not already sorted)
    arr1_sorted = np.sort(arr1)
    arr2_sorted = np.sort(arr2)
    
    for element in arr1_sorted:
        while index < len(arr2_sorted) and arr2_sorted[index] < element:
            index += 1
        if index < len(arr2_sorted) and arr2_sorted[index] == element:
            index += 1
        else:
            missing_indices.append(np.where(arr1 == element)[0][0])
    
    return missing_indices

dup = find_missing_indices(ovenxold, ovenx)
oveny = np.delete(ovenyold, dup)

interpolated_function = interp.interp1d(ovenx, oveny, kind='quadratic', fill_value="extrapolate")
x_val = np.linspace(min(ovenx), max(ovenx), 100)
y_val = interpolated_function(oveny)
coeffs = np.polyfit(ovenx, oveny, deg=3)
oven = sum(c * F.x**i for i, c in enumerate(coeffs[::-1]))
print(oven)

# plt.plot(ovenx, oveny)
plt.plot(ovenxold, ovenyold)
plt.plot(ovenx, -1.52104898102707e+22*ovenx**3 + 1.5758859094432e+23*ovenx**2 - 6.6282715504034e+18*ovenx + 1.27672191982656e+24)
plt.show()
