import matplotlib.pyplot as plt
import numpy as np
import festim as F
import numpy as np
import sympy as sp
from festim import x,y,z,t
my_model = F.Simulation()
results_folder = "Cm measurements"
data17 = np.genfromtxt(
    results_folder + f'/Cm17.0.txt', skip_header=1, delimiter=","
)
data18 = np.genfromtxt(
    results_folder + f'/Cm18.0.txt', skip_header=1, delimiter=","
)
data19 = np.genfromtxt(
    results_folder + f'/Cm19.0.txt', skip_header=1, delimiter=","
)
data20 = np.genfromtxt(
    results_folder + f'/Cm20.0.txt', skip_header=1, delimiter=","
)
data21 = np.genfromtxt(
    results_folder + f'/Cm21.0.txt', skip_header=1, delimiter=","
)
data22 = np.genfromtxt(
    results_folder + f'/Cm22.0.txt', skip_header=1, delimiter=","
)
data23 = np.genfromtxt(
    results_folder + f'/Cm23.0.txt', skip_header=1, delimiter=","
)

fig, axs = plt.subplots(3, 3)
axs[0, 0].plot(data17[:, 0], data17[:, 50])
axs[0, 0].plot(data17[:, 0], data17[:, 40])
axs[0, 0].plot(data17[:, 0], data17[:, 30])
axs[0, 0].plot(data17[:, 0], data17[:, 20])
axs[0, 0].set_title('Cm = 1e17', loc = 'right')
axs[0, 1].plot(data18[:, 0], data18[:, 50])
axs[0, 1].plot(data18[:, 0], data18[:, 40])
axs[0, 1].plot(data18[:, 0], data18[:, 30])
axs[0, 1].plot(data18[:, 0], data18[:, 20])
axs[0, 1].set_title('Cm = 1e18', loc = 'right')
axs[0, 2].plot(data19[:, 0], data19[:, 50])
axs[0, 2].plot(data19[:, 0], data19[:, 40])
axs[0, 2].plot(data19[:, 0], data19[:, 30])
axs[0, 2].plot(data19[:, 0], data19[:, 20])
axs[0, 2].set_title('Cm = 1e19', loc = 'right')
axs[1, 0].plot(data20[:, 0], data20[:, 50])
axs[1, 0].plot(data20[:, 0], data20[:, 40])
axs[1, 0].plot(data20[:, 0], data20[:, 30])
axs[1, 0].plot(data20[:, 0], data20[:, 20])
axs[1, 0].set_title('Cm = 1e20', loc = 'right')
axs[1, 1].plot(data21[:, 0], data21[:, 50])
axs[1, 1].plot(data21[:, 0], data21[:, 40])
axs[1, 1].plot(data21[:, 0], data21[:, 30])
axs[1, 1].plot(data21[:, 0], data21[:, 20])
axs[1, 1].set_title('Cm = 1e21', loc = 'right')
axs[1, 2].plot(data22[:, 0], data22[:, 50])
axs[1, 2].plot(data22[:, 0], data22[:, 40])
axs[1, 2].plot(data22[:, 0], data22[:, 30])
axs[1, 2].plot(data22[:, 0], data22[:, 20])
axs[1, 2].set_title('Cm = 1e22', loc = 'right')
axs[2, 0].plot(data23[:, 0], data23[:, 50])
axs[2, 0].plot(data23[:, 0], data23[:, 40])
axs[2, 0].plot(data23[:, 0], data23[:, 30])
axs[2, 0].plot(data23[:, 0], data23[:, 20])
axs[2, 0].set_title('Cm = 1e23', loc = 'right')

for ax in axs.flat:
    ax.set(xlabel='r/m', ylabel='Mobile concentration (H/m3)')


# plt.plot(data[:, 0], data[:, 50])
# plt.plot(data[:, 0], data[:, 40])
# plt.plot(data[:, 0], data[:, 30])
# plt.plot(data[:, 0], data[:, 20])
# plt.xlabel("x (m)")
# plt.ylabel("Mobile concentration (H/m3)")
# plt.title(h)
plt.show()