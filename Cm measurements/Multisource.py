import festim as F
my_model = F.Simulation()
import numpy as np
import sympy as sp
from festim import x,y,z,t
T_b = 975#K
r_p = 3e-2#m
S = 1.715e17
g_atom_density = 1.1e29
def arrmax(A):
    maxi = float('-inf')  # Initialize maxi as negative infinity
    for num in A:
        if num > maxi:
            maxi = num
    return maxi

for t_res_day in range(25,501,25):
    t_res = t_res_day*24*3600
    size = np.sqrt(3)*r_p #sqrt 3 is calculated from primitive cubic arrangement
    t = np.arange(0,t_res,t_res/10)
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

    my_model.boundary_conditions = [F.FluxBC(surfaces=2, value=0, field ='0')]

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
        final_time=t_res, # s
        chemical_pot=True
        )
    my_model.dt = F.Stepsize(t_res/10)  # s
    results_folder = "Multioven"
    my_model.exports = [
        F.XDMFExport(
            field="solute",
            filename=results_folder + f'/pebble{t_res_day}.xdmf',
            checkpoint=True  # needed in 1D
            ),
        F.TXTExport(field="solute", times=t.tolist(), filename=results_folder+ f'/pebble{t_res_day}.txt')
    ]
    my_model.initialise()

    my_model.run()
# import matplotlib.pyplot as plt
# import numpy as np

# data = np.genfromtxt(
#     results_folder + f'/Flux.txt', skip_header=1, delimiter=","
# )

# profile = data[:,0]
# p = arrmax(max(np.asarray(np.where(profile == r_p))))
# print("Cm = ", max(tuple(data[p:,len(data[0])-1])))

# plt.plot(data[:, 0], data[:, 9])
# plt.plot(data[:, 0], data[:, 7])
# plt.plot(data[:, 0], data[:, 5])
# plt.plot(data[:, 0], data[:, 3])
# plt.plot(data[:, 0], data[:, 1])
# plt.xlabel("x (m)")
# plt.ylabel("Mobile concentration (H/m3)")
# plt.yscale('log')
# plt.show()