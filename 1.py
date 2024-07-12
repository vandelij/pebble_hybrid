# pebble dimensions: TRISO radius of 2.5cm, pebble radius of 3cm
# Key parameters: T_b, t_res, r_p, S,

#To upload:
#git add .
#git status
#git commit -m "insert message"
#git push
#To pull:
#git pull
#to go to a new branch:
#git checkout new_branch

# GRAPHITE:
#         Author: Petucci
#         Material: carbon
#         Year: 2013
#         Isotope: H
#         Pre-exponential factor: 1.16×10⁻⁶ m²/s
#         Activation energy: 3.51×10⁻² eV/particle

# LIPB:
#         Author: Edao
#         Material: lipb
#         Year: 2011
#         Isotope: H
#         Pre-exponential factor: 7.88×10⁻⁸ m²/s
#         Activation energy: 1.64×10⁻¹ eV/particle

import festim as F
my_model = F.Simulation()
import numpy as np
import sympy as sp
from festim import x,y,z,t
T_b = 1000#K
t_res = 1000#s
r_p = 3e-2 #m
S = 1e22
g_atom_density = 1.1e29

size = 3.5e-2
t = np.arange(0,t_res,10)
x = np.arange(0,size,size/100)
my_model.mesh = F.MeshFromVertices(np.linspace(0, size, num=1001), type = 'spherical')

graphite = F.Material(
    id=1,
    D_0= 1.16e-6,
    E_D= 3.51e-2,
    borders=[0, r_p],
)
lipb = F.Material(
    id=2,
    D_0= 7.88e-8,
    E_D= 1.64e-1,
    borders=[r_p, size],
)

my_model.materials = F.Materials([graphite, lipb])

my_model.T = F.Temperature(value=T_b)
# my_model.boundary_conditions = [
#     F.DirichletBC(
#         surfaces=1,
#         value=1e24,  # H/m3/s
#         field=0
#         )
# ]

# trap_1 = F.Trap(
#     k_0=graphite.D_0 / (1.1e-10**2 * 6 * g_atom_density),
#     E_k=graphite.E_D,
#     p_0=5e12,
#     E_p=3.3,
#     density=1.85e-8*g_atom_density,
#     materials=graphite,
# )

# trap_2 = F.Trap(
#     k_0=graphite.D_0 / (1.1e-10**2 * 6 * g_atom_density),
#     E_k=graphite.E_D,
#     p_0=1e4,
#     E_p=1.6,
#     density=1.5e-8*g_atom_density,
#     materials=graphite,
# )

# trap_3 = F.Trap(
#     k_0=graphite.D_0 / (1.1e-10**2 * 6 * g_atom_density),
#     E_k=graphite.E_D,
#     p_0=1e5,
#     E_p=1.3,
#     density=9e-9*g_atom_density,
#     materials=graphite,
# )

# my_model.traps = [trap_1, trap_2, trap_3]

my_model.sources = [F.Source(value=S, volume=2, field=0)]
#my_model.sources = [F.InitialCondition(field='mobile', value=F.x)]
my_model.settings = F.Settings(
    absolute_tolerance=1e10,
    relative_tolerance=1e-10,
    final_time=500  # s
    )
my_model.dt = F.Stepsize(2)  # s
results_folder = "task01"
my_model.exports = [
    F.XDMFExport(
        field="solute",
        filename=results_folder + "/hydrogen_concentration.xdmf",
        checkpoint=False  # needed in 1D
        ),
    F.TXTExport(field="solute", times=t.tolist(), filename=results_folder+"/mobile_concentration.txt")
]
my_model.initialise()

my_model.run()
import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt(
    results_folder + "/mobile_concentration.txt", skip_header=1, delimiter=","
)

# plt.ylim(0, 5e24)
# plt.plot(data[:, 0], data[:, 50], label="1.0 s")
# plt.plot(data[:, 0], data[:, 40], label="0.5 s")
# plt.plot(data[:, 0], data[:, 30], label="0.2 s")
# plt.plot(data[:, 0], data[:, 20], label="0.1 s")
# plt.xlabel("x (m)")
# plt.ylabel("Mobile concentration (H/m3)")
# plt.show()

####
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Load the simulation results from the TXT file
data = np.genfromtxt(results_folder + "/mobile_concentration.txt", skip_header=1, delimiter=",")

# Check the shape of the data to avoid index errors
num_frames = data.shape[1] - 1  # Number of datasets excluding the first column

# Set up the figure and axis
fig, ax = plt.subplots()
heatmap = ax.imshow(data[:, 1].reshape(1, -1), aspect = 'auto', cmap='jet', origin='lower',interpolation='nearest')
border = plt.axvline(x=1000, linewidth = 3, color='black')

# Add color bar
cbar = plt.colorbar(heatmap)
cbar.set_label('Concentration (H/m³)')
border1 = plt.axvline(x=1714, linewidth = 3, color='black')
border2 = plt.axvline(x=1429, linewidth = 3, color='black')

# Update function for animation
def update(frame):
    if frame < num_frames:
        # Update the heatmap data with the next dataset
        heatmap.set_array(data[:, frame + 1].reshape(1, -1))
        return [heatmap, border1, border2]
    


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=500, blit=True)
writer = animation.PillowWriter(fps=5)
ani.save('animation.wmv', writer=writer)

# Display the animation
plt.show()








