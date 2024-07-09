import h_transport_materials as htm

D = (
    htm.diffusivities.filter(material="carbon")
    .filter(isotope="h")
    .filter(author="petucci")[0]
)
print(D)

import festim as F
import numpy as np

import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)


def TDS(n, E_p):
    """Runs the simulation with parameters p that represent:

    Args:
        n (float): concentration of trap 1, at. fr.
        E_p (float): detrapping barrier from trap 1, eV

    Returns:
        F.DerivedQuantities: the derived quantities of the simulation
    """
    g_atom_density = 1.1e29  # atom/m3
    trap_conc = n * g_atom_density

    # Define Simulation object
    synthetic_TDS = F.Simulation()

    # Define a simple mesh
    vertices = np.linspace(0, 20e-6, num=200)
    synthetic_TDS.mesh = F.MeshFromVertices(vertices)

    # Define material properties
    graphite = F.Material(
        id=1,
        D_0=D.pre_exp.magnitude,
        E_D=D.act_energy.magnitude,
    )
    synthetic_TDS.materials = graphite

    # Define traps
    trap_1 = F.Trap(
        k_0=D.pre_exp.magnitude / (1.1e-10**2 * 6 * g_atom_density),
        E_k=D.act_energy.magnitude,
        p_0=1e13,
        E_p=E_p,
        density=trap_conc,
        materials=graphite
    )

    synthetic_TDS.traps = [trap_1]

    # Set initial conditions
    synthetic_TDS.initial_conditions = [
        F.InitialCondition(field="1", value=trap_conc),
    ]

    # Set boundary conditions
    synthetic_TDS.boundary_conditions = [
        F.DirichletBC(surfaces=[1, 2], value=0, field=0)
    ]

    # Define the material temperature evolution
    ramp = 10  # K/s
    synthetic_TDS.T = F.Temperature(value=900 + ramp * (F.t))

    # Define the simulation settings
    synthetic_TDS.dt = F.Stepsize(
        initial_value=0.01,
        stepsize_change_ratio=1.2,
        max_stepsize=lambda t: None if t < 1 else 1,
        dt_min=1e-6,
    )

    synthetic_TDS.settings = F.Settings(
        absolute_tolerance=1e10,
        relative_tolerance=1e-10,
        final_time=140,
        maximum_iterations=50,
    )

    # Define the exports
    derived_quantities = F.DerivedQuantities(
        [
            F.HydrogenFlux(surface=1),
            F.HydrogenFlux(surface=2),
            F.AverageVolume(field="T", volume=1),
        ]
    )

    synthetic_TDS.exports = [derived_quantities]
    synthetic_TDS.initialise()
    synthetic_TDS.run()

    return derived_quantities

# Get the flux dependence
reference_prms = [1e-2, 1.0]
data = TDS(*reference_prms)

import matplotlib.pyplot as plt
import os 

# Get temperature
T = data.filter(fields="T").data

# Calculate the total desorptio flux
flux_left = data.filter(fields="solute", surfaces=1).data
flux_right = data.filter(fields="solute", surfaces=2).data
flux_total = -(np.array(flux_left) + np.array(flux_right))

# Add random noise
noise = np.random.normal(0, 0.05 * max(flux_total), len(flux_total))
noisy_flux = flux_total + noise



ref = np.genfromtxt("g.csv", delimiter=",")

def info(i, p):
    """
    Print information during the fitting procedure
    """
    print("-" * 40)
    print(f"i = {i}")
    print("New simulation.")
    print(f"Point is: {p}")

from scipy.interpolate import interp1d

prms = []
errors = []


def error_function(prm):
    """
    Compute average absolute error between simulation and reference
    """
    global i
    global prms
    global errors
    prms.append(prm)
    i += 1
    info(i, prm)

    # Filter the results if a negative value is found
    if any([e < 0 for e in prm]):
        return 1e30

    # Get the simulation result
    n, Ep = prm
    res = TDS(n, Ep)

    T = np.array(res.filter(fields="T").data)
    flux = -np.array(res.filter(fields="solute", surfaces=1).data) - np.array(
        res.filter(fields="solute", surfaces=2).data
    )

    # Plot the intermediate TDS spectra
    if i == 1:
        plt.plot(T, flux, color="tab:red", lw=2, label="Initial guess")
    else:
        plt.plot(T, flux, color="tab:grey", lw=0.5)
        plt.plot(ref[:, 0], ref[:, 1], linewidth=2, label="Reference")
    plt.show(block=False)
    plt.pause(3)
    plt.close()

    interp_tds = interp1d(T, flux, fill_value="extrapolate")

    # Compute the mean absolute error between sim and ref
    err = np.abs(interp_tds(ref[:, 0]) - ref[:, 1]).mean()

    print(f"Average absolute error is : {err:.2e}")
    errors.append(err)
    return err

from scipy.optimize import minimize

i = 0  # initialise counter

# Set the tolerances
fatol = 1e18
xatol = 1e-3

initial_guess = [2e-8, 2.5]

# Minimise the error function
res = minimize(
    error_function,
    np.array(initial_guess),
    method="Nelder-Mead",
    options={"disp": True, "fatol": fatol, "xatol": xatol},
)

# Process the obtained results
predicted_data = TDS(*res.x)

T = predicted_data.filter(fields="T").data

flux_left = predicted_data.filter(fields="solute", surfaces=1).data
flux_right = predicted_data.filter(fields="solute", surfaces=2).data
flux_total = -(np.array(flux_left) + np.array(flux_right))

# Visualise
plt.plot(ref[:, 0], ref[:, 1], linewidth=2, label="Reference")
plt.plot(T, flux_total, linewidth=2, label="Optimised")

plt.ylabel(r"Desorption flux (m$^{-2}$ s$^{-1}$)")
plt.xlabel(r"Temperature (K)")
plt.legend()
plt.show()

