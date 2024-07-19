#With the entire ball at temp T for time t, how much tritium is released
#np.trapz() for integral
# Use mass transfer BC: tritium mass flux J = K*Cs, K is mass transfer coeff and Cs is surface conc
#Figure out k
#gas: argon


import festim as F
my_model = F.Simulation()
import numpy as np
import sympy as sp
from festim import x,y,z,t
import scipy.interpolate as interp
import matplotlib.pyplot as plt
r_p = 3e-2#m
def arrmax(A):
    maxi = float('-inf')  # Initialize maxi as negative infinity
    for num in A:
        if num > maxi:
            maxi = num
    return maxi

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
print("Oven function = ", oven)

temp = 200 #degrees Celsius
time = 2e6#s
step = 50000
alpha = 0.50 #Reynolds exponent, 0.5 for laminar and 1.0 for turbulent
gamma = 0.33 #Schmidt exponent, 0.33 for sphere
C = 0.552
mu = (0.00629075*temp + 2.10264)*(10**-5) #Pa s, dynamic viscosity (temp-dependent)
rho = 1.613 #kg/m3, density
h = r_p*2 #m, pebble diameter over which carrier gas flows
D = 7.7e-5 # m2/s, diffusion coefficient
Dh = h #m, hydraulic diameter of gas flow channels
U0 = 10 #m/s, carrier gas flow velocity
Sh0 = 2.0 
Sc = mu/(rho*D)
Re = (Dh*rho*U0)/(mu)
Sh = C*(Re**(alpha))*(Sc**(gamma)) + Sh0 #All values taken from Frossling eqn for spheres
K= (Sh*D)/h
print("K =",K)
g_atom_density = 1.1e29
size = r_p
Cs=oveny[-1]
print("Cs = ", Cs)
t = np.arange(0,time,step)
vertices = np.linspace(0,r_p, num = 100)
my_model.mesh = F.MeshFromVertices(vertices, type = 'spherical')

my_model.initial_conditions = [F.InitialCondition(
    field = '0', 
    value = oven,
)]

graphite = F.Material(
    id=1,
    D_0= 1.16e-6,
    E_D= 3.51e-2,
    S_0=5.73e22, 
    E_S=-1.89e-01, 
    borders=[0, r_p],
)

my_model.materials = F.Materials([graphite])

my_model.T = F.Temperature(value=temp+273.15)
my_model.boundary_conditions = [
    F.FluxBC(surfaces=2, value=K*Cs*6.02e23, field='0')
]


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

my_model.settings = F.Settings(
    absolute_tolerance=1e10,
    relative_tolerance=1e-10,
    final_time=time, # s
    chemical_pot=False
    )
my_model.dt = F.Stepsize(step)  # s
results_folder = "Oven data"
my_model.exports = [
    F.XDMFExport(
        field="0",
        filename=results_folder + '/oven.xdmf',
        checkpoint=False  # needed in 1D
        ),
    F.TXTExport(field="0", times=t.tolist(), filename=results_folder+'/oven.txt')
]

my_model.initialise()
my_model.run()
import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt(
    results_folder + '/oven.txt', skip_header=1, delimiter=","
)

#plt.plot(data[:, 0], data[:, len(data[0])-1])
plt.plot(data[:, 0], data[:, 3])
plt.plot(data[:, 0], data[:, 2])
plt.plot(data[:, 0], data[:, 1],marker = '.')
plt.plot(ovenx, oveny)
plt.xlabel("x (m)")
plt.ylabel("Mobile concentration (H/m3)")
plt.yscale('log')
plt.show()