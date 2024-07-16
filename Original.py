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
Cm = 1e20 #concentration at infinity

size = 3.5e-2
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

data = np.genfromtxt(
    results_folder + f'/Cm{np.log10(float(Cm))}.txt', skip_header=1, delimiter=","
)


plt.plot(data[:, 0], data[:, 50])
plt.plot(data[:, 0], data[:, 40])
plt.plot(data[:, 0], data[:, 30])
plt.plot(data[:, 0], data[:, 20])
plt.xlabel("x (m)")
plt.ylabel("Mobile concentration (H/m3)")
plt.show()