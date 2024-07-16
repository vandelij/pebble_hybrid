# TODO:
# - Automate code to loop diff Cm from 1e17, 1e18, 1e19 ... 1e23
# - Save as files with diff file names
# - hint: f'cm{xxx}'
# - implement zero diffusion flux boundary condition (3D geometry thing)
# - match Cinf (point where local minima asymptotes) from 0-flux BC to other Cinf
# - Oven ramp: 900 - 1700 K
# - Multistage heating oven(?)
# - Email Prof Shirvan for oven heating range
# - 


import festim as F
my_model = F.Simulation()
import numpy as np
import sympy as sp
from festim import x,y,z,t
T_b = 975#K
t_res = 1000#s
r_p = 3e-2#m
S = 1.715e17
g_atom_density = 1.1e29
for h in range(17,24):
    Cm = "{:e}".format(10**h) #concentration at infinity

    size = np.sqrt(3)*r_p
    t = np.arange(0,t_res,10)
    x = np.arange(0,size,size/100)
    vertices_g = np.linspace(0,r_p, num = 100)
    vertices_lipb = np.linspace(r_p,size, num = 100)
    vertices = np.concatenate([vertices_g, vertices_lipb])
    my_model.mesh = F.MeshFromVertices(vertices, type = 'spherical')

    graphite = F.Material(
        id=1,
        D_0= 1.16e-6,
        E_D= 3.51e-2,
        S_0=5.73e22, 
        E_S=-1.89e-01, 
        borders=[0, r_p],
    )
    lipb = F.Material(
        id=2,
        D_0= 7.88e-8,
        E_D= 1.64e-1,
        S_0=5.30e22,
        E_S=5.95e-01, 
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

    my_model.boundary_conditions = [
        F.DirichletBC(surfaces=2, value=Cm, field='solute')
    ]

    # my_model.boundary_conditions = [
    #     # F.SievertsBC(
    #         # surfaces=1, 
    #         # S_0=5.73e22, 
    #         # E_S=-1.89e-01, 
    #         # pressure=P,
    #         # ) , 
    #     F.SievertsBC(
    #         surfaces=2, 
    #         S_0=5.30e22,
    #         E_S=5.95e-01, 
    #         pressure=P,
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
        final_time=500, # s
        chemical_pot=True
        )
    my_model.dt = F.Stepsize(2)  # s
    results_folder = "Cm measurements"
    my_model.exports = [
        F.XDMFExport(
            field="solute",
            filename=results_folder + f'/Cm{np.log10(float(Cm))}.xdmf',
            checkpoint=False  # needed in 1D
            ),
        F.TXTExport(field="solute", times=t.tolist(), filename=results_folder+f'/Cm{np.log10(float(Cm))}.txt')
    ]
    my_model.initialise()

    my_model.run()
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
axs[0, 0].set_title('17')
axs[0, 1].plot(data18[:, 0], data18[:, 50])
axs[0, 1].plot(data18[:, 0], data18[:, 40])
axs[0, 1].plot(data18[:, 0], data18[:, 30])
axs[0, 1].plot(data18[:, 0], data18[:, 20])
axs[0, 1].set_title('18')
axs[0, 2].plot(data19[:, 0], data19[:, 50])
axs[0, 2].plot(data19[:, 0], data19[:, 40])
axs[0, 2].plot(data19[:, 0], data19[:, 30])
axs[0, 2].plot(data19[:, 0], data19[:, 20])
axs[0, 2].set_title('19')
axs[1, 0].plot(data20[:, 0], data20[:, 50])
axs[1, 0].plot(data20[:, 0], data20[:, 40])
axs[1, 0].plot(data20[:, 0], data20[:, 30])
axs[1, 0].plot(data20[:, 0], data20[:, 20])
axs[1, 0].set_title('20')
axs[1, 1].plot(data21[:, 0], data21[:, 50])
axs[1, 1].plot(data21[:, 0], data21[:, 40])
axs[1, 1].plot(data21[:, 0], data21[:, 30])
axs[1, 1].plot(data21[:, 0], data21[:, 20])
axs[1, 1].set_title('21')
axs[1, 2].plot(data22[:, 0], data22[:, 50])
axs[1, 2].plot(data22[:, 0], data22[:, 40])
axs[1, 2].plot(data22[:, 0], data22[:, 30])
axs[1, 2].plot(data22[:, 0], data22[:, 20])
axs[1, 2].set_title('22')
axs[2, 0].plot(data23[:, 0], data23[:, 50])
axs[2, 0].plot(data23[:, 0], data23[:, 40])
axs[2, 0].plot(data23[:, 0], data23[:, 30])
axs[2, 0].plot(data23[:, 0], data23[:, 20])
axs[2, 0].set_title('23')

for ax in axs.flat:
    ax.set(xlabel='x-label', ylabel='y-label')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

# plt.plot(data[:, 0], data[:, 50])
# plt.plot(data[:, 0], data[:, 40])
# plt.plot(data[:, 0], data[:, 30])
# plt.plot(data[:, 0], data[:, 20])
# plt.xlabel("x (m)")
# plt.ylabel("Mobile concentration (H/m3)")
# plt.title(h)
plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# data = np.genfromtxt(
#     results_folder + f'/Cm{np.log10(float(Cm))}.txt', skip_header=1, delimiter=","
# )


# plt.plot(data[:, 0], data[:, 50])
# plt.plot(data[:, 0], data[:, 40])
# plt.plot(data[:, 0], data[:, 30])
# plt.plot(data[:, 0], data[:, 20])
# plt.xlabel("x (m)")
# plt.ylabel("Mobile concentration (H/m3)")
# plt.show()

####
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation

# # Load the simulation results from the TXT file
# data = np.genfromtxt(results_folder + "/mobile_concentration.txt", skip_header=1, delimiter=",")

# # Check the shape of the data to avoid index errors
# num_frames = data.shape[1] - 1  # Number of datasets excluding the first column

# # Set up the figure and axis
# fig, ax = plt.subplots()
# heatmap = ax.imshow(data[:, 1].reshape(1, -1), aspect = 'auto', cmap='jet', origin='lower',interpolation='nearest')

# # Add color bar
# cbar = plt.colorbar(heatmap)
# cbar.set_label('Concentration (H/m³)')
# border1 = plt.axvline(x=1714, linewidth = 3, color='black')
# border2 = plt.axvline(x=1429, linewidth = 3, color='black')

# # Update function for animation
# def update(frame):
#     if frame < num_frames:
#         # Update the heatmap data with the next dataset
#         heatmap.set_array(data[:, frame + 1].reshape(1, -1))
#         return [heatmap, border1, border2]
    


# # Create the animation
# ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=100, blit=True)
# writer = animation.PillowWriter(fps=5)
# ani.save('animation.gif', writer=writer)

# # Display the animation
# plt.show()

####

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