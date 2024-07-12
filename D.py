import h_transport_materials as htm

D = (
    htm.solubilities.filter(material="lipb")
    .filter(isotope="d")
    .filter(author="okada")[0]
)
print(D)

#https://htm-dashboard-uan5l4xr6a-od.a.run.app/