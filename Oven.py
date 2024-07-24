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

def OVEN(x):
    return sum(c * x**i for i, c in enumerate(coeffs[::-1]))

temp = 70 #degrees Celsius, PARAMETER 1
time = 2e2#s, PARAMETER 2
step = time/20
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
    F.MassFlux(h_coeff=K, c_ext=0, surfaces=2)
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
    chemical_pot=True
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
xdata = data[:,0]
initialdata = data[:, 1]
finaldata = data[:, len(data[0])-1]
N = np.trapz(y = initialdata, x = xdata) - np.trapz(y = finaldata, x = xdata)

print(N)
####
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Load the simulation results from the TXT file
data = np.genfromtxt(results_folder + "/oven.txt", skip_header=1, delimiter=",")

# Check the shape of the data to avoid index errors
num_frames = data.shape[1] - 1  # Number of datasets excluding the first column

# Set up the figure and axis
fig, ax = plt.subplots()
heatmap = ax.imshow(data[:, 1].reshape(1, -1), aspect = 'auto', cmap='jet', origin='lower',interpolation='nearest')
plt.xlim(0,197)
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
ani.save('animation.gif', writer=writer)

# Display the animation
plt.show()

####

# plt.plot(data[:, 0], data[:, len(data[0])-1])
# # plt.plot(data[:, 0], data[:, 7])
# # plt.plot(data[:, 0], data[:, 6])
# # plt.plot(data[:, 0], data[:, 5])
# # plt.plot(data[:, 0], data[:, 4])
# # plt.plot(data[:, 0], data[:, 3])
# # plt.plot(data[:, 0], data[:, 2])
# plt.plot(data[:, 0], data[:, 1])
# # plt.plot(ovenx, oveny)
# # plt.plot(ovenx, OVEN(ovenx))
# plt.xlabel("x (m)")
# plt.ylabel("Mobile concentration (H/m3)")
# plt.yscale('log')
# plt.show()