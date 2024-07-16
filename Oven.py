#- instead of source term, use an initial condition term: https://festim.readthedocs.io/en/v1.2.1/userguide/initial_conditions.html#
import festim as F
my_model = F.Simulation()
import numpy as np

vertices = np.concatenate([
    np.linspace(0, 20e-6, num=2000),
])

my_model.mesh = F.MeshFromVertices(vertices)
graphite = F.Material(
    id=1,
    D_0= 1.16e-6,
    E_D= 3.51e-2,
)

my_model.materials = graphite
import sympy as sp

implantation_time = 400  # s

ion_flux = sp.Piecewise((1.715e17, F.t <= implantation_time), (0, True))

source_term = F.ImplantationFlux(
    flux=ion_flux,  # H/m2/s
    imp_depth=4.5e-9,  # m
    width=2.5e-9,  # m
    volume=1
)

my_model.sources = [source_term]

g_atom_density = 1.1e29

trap_1 = F.Trap(
    k_0=graphite.D_0 / (1.1e-10**2 * 6 * g_atom_density),
    E_k=graphite.E_D,
    p_0=5e12,
    E_p=3.3,
    density=1.85e-8*g_atom_density,
    materials=graphite,
)

trap_2 = F.Trap(
    k_0=graphite.D_0 / (1.1e-10**2 * 6 * g_atom_density),
    E_k=graphite.E_D,
    p_0=1e4,
    E_p=1.6,
    density=1.5e-8*g_atom_density,
    materials=graphite,
)

trap_3 = F.Trap(
    k_0=graphite.D_0 / (1.1e-10**2 * 6 * g_atom_density),
    E_k=graphite.E_D,
    p_0=1e5,
    E_p=1.3,
    density=9e-9*g_atom_density,
    materials=graphite,
)

my_model.traps = [trap_1, trap_2, trap_3]

my_model.boundary_conditions = [
    F.DirichletBC(surfaces=[1, 2], value=0, field=0)
]
implantation_temp = 500  # K
temperature_ramp = 80  # K/s

start_tds = implantation_time + 50  # s

my_model.T = F.Temperature(
    value=sp.Piecewise(
        (implantation_temp, F.t < start_tds),
        (implantation_temp + temperature_ramp*(F.t-start_tds), True))
)

my_model.dt = F.Stepsize(
    initial_value=0.5,
    stepsize_change_ratio=1.1,
    max_stepsize=lambda t: 0.5 if t > start_tds else None,
    dt_min=1e-05,
    milestones=[implantation_time, start_tds],
)
my_model.settings = F.Settings(
    absolute_tolerance=1e10,
    relative_tolerance=1e-10,
    final_time=500
)

list_of_derived_quantities = [
        F.TotalVolume("solute", volume=1),
        F.TotalVolume("retention", volume=1),
        F.TotalVolume("1", volume=1),
        F.TotalVolume("2", volume=1),
        F.TotalVolume("3", volume=1),
        F.HydrogenFlux(surface=1),
        F.HydrogenFlux(surface=2)
    ]

derived_quantities = F.DerivedQuantities(
    list_of_derived_quantities,
    # filename="tds/derived_quantities.csv"  # optional set a filename to export the data to csv
)


my_model.exports = [derived_quantities]
my_model.initialise()
my_model.run()
t = derived_quantities.t
flux_left = derived_quantities.filter(fields="solute", surfaces=1).data
flux_right = derived_quantities.filter(fields="solute", surfaces=2).data

flux_total = -np.array(flux_left) - np.array(flux_right)
import matplotlib.pyplot as plt
plt.plot(t, flux_total, linewidth=3)

plt.ylabel(r"Desorption flux (m$^{-2}$ s$^{-1}$)")
plt.xlabel(r"Time (s)")
trap_1 = derived_quantities.filter(fields="1").data
trap_2 = derived_quantities.filter(fields="2").data
trap_3 = derived_quantities.filter(fields="3").data

contribution_trap_1 = -np.diff(trap_1)/np.diff(t)
contribution_trap_2 = -np.diff(trap_2)/np.diff(t)
contribution_trap_3 = -np.diff(trap_3)/np.diff(t)

plt.plot(t, flux_total, linewidth=3)
plt.plot(t[1:], contribution_trap_1, linestyle="--", color="grey")
plt.fill_between(t[1:], 0, contribution_trap_1, facecolor='grey', alpha=0.1)
plt.plot(t[1:], contribution_trap_2, linestyle="--", color="grey")
plt.fill_between(t[1:], 0, contribution_trap_2, facecolor='grey', alpha=0.1)
plt.plot(t[1:], contribution_trap_3, linestyle="--", color="grey")
plt.fill_between(t[1:], 0, contribution_trap_3, facecolor='grey', alpha=0.1)

# plt.xlim(450, 500)
# plt.ylim(bottom=-1.25e18, top=0.6e19)
# plt.ylabel(r"Desorption flux (m$^{-2}$ s$^{-1}$)")
# plt.xlabel(r"Time (s)")

plt.ylabel(r"Desorption flux (m$^{-2}$ s$^{-1}$)")
plt.xlabel(r"Time (s)")
plt.show()