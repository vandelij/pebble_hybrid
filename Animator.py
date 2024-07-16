import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
results_folder = "Cm measurements"
h=23

####
# data17 = np.genfromtxt(
#     results_folder + f'/Cm17.0.txt', skip_header=1, delimiter=","
# )
# data18 = np.genfromtxt(
#     results_folder + f'/Cm18.0.txt', skip_header=1, delimiter=","
# )
# data19 = np.genfromtxt(
#     results_folder + f'/Cm19.0.txt', skip_header=1, delimiter=","
# )
# data20 = np.genfromtxt(
#     results_folder + f'/Cm20.0.txt', skip_header=1, delimiter=","
# )
# data21 = np.genfromtxt(
#     results_folder + f'/Cm21.0.txt', skip_header=1, delimiter=","
# )
# data22 = np.genfromtxt(
#     results_folder + f'/Cm22.0.txt', skip_header=1, delimiter=","
# )
# data23 = np.genfromtxt(
#     results_folder + f'/Cm23.0.txt', skip_header=1, delimiter=","
# )
# num_frames = data17.shape[1] - 1
# # Set up the figure and axis
# fig, ax = plt.subplots(3,3)
# heatmap1 = ax.imshow(data17[:, 1].reshape(1, -1), aspect = 'auto', cmap='jet', origin='lower',interpolation='nearest')
# heatmap2 = ax.imshow(data18[:, 1].reshape(1, -1), aspect = 'auto', cmap='jet', origin='lower',interpolation='nearest')
# heatmap3 = ax.imshow(data19[:, 1].reshape(1, -1), aspect = 'auto', cmap='jet', origin='lower',interpolation='nearest')
# heatmap4 = ax.imshow(data20[:, 1].reshape(1, -1), aspect = 'auto', cmap='jet', origin='lower',interpolation='nearest')
# heatmap5 = ax.imshow(data21[:, 1].reshape(1, -1), aspect = 'auto', cmap='jet', origin='lower',interpolation='nearest')
# heatmap6 = ax.imshow(data22[:, 1].reshape(1, -1), aspect = 'auto', cmap='jet', origin='lower',interpolation='nearest')
# heatmap7 = ax.imshow(data23[:, 1].reshape(1, -1), aspect = 'auto', cmap='jet', origin='lower',interpolation='nearest')

# cbar = plt.colorbar(heatmap1)
# cbar.set_label('Concentration (H/m³)')
# def update(frame):
#     if frame < num_frames:
#         # Update the heatmap data with the next dataset
#         heatmap1.set_array(data17[:, frame + 1].reshape(1, -1))
#         heatmap2.set_array(data18[:, frame + 1].reshape(1, -1))
#         heatmap3.set_array(data19[:, frame + 1].reshape(1, -1))
#         heatmap4.set_array(data20[:, frame + 1].reshape(1, -1))
#         heatmap5.set_array(data21[:, frame + 1].reshape(1, -1))
#         heatmap6.set_array(data22[:, frame + 1].reshape(1, -1))
#         heatmap7.set_array(data23[:, frame + 1].reshape(1, -1))
#         return [heatmap1,heatmap2,heatmap3,heatmap4,heatmap5,heatmap6,heatmap7,]
# ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=250, blit=True)
# writer = animation.PillowWriter(fps=5)
# ani.save('animation.gif', writer=writer)

# # Display the animation
# plt.show()

####
# Load the simulation results from the TXT file
data = np.genfromtxt(results_folder + f'/Cm{float(h)}.txt', skip_header=1, delimiter=",")

# Check the shape of the data to avoid index errors
num_frames = data.shape[1] - 1  # Number of datasets excluding the first column

# Set up the figure and axis
fig, ax = plt.subplots()
heatmap = ax.imshow(data[:, 1].reshape(1, -1), vmin=0, vmax =0.1e20, aspect = 'auto', cmap='jet', origin='lower',interpolation='nearest')

# Add color bar
cbar = plt.colorbar(heatmap)
cbar.set_label('Concentration (H/m³)')
border1 = plt.axvline(x=200, linewidth = 3, color='black')
plt.xlim(0,300)

# Update function for animation
def update(frame):
    if frame < num_frames:
        # Update the heatmap data with the next dataset
        heatmap.set_array(data[:, frame + 1].reshape(1, -1))
        return [heatmap, border1]
    


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=250, blit=True)
writer = animation.PillowWriter(fps=5)
ani.save('animation.gif', writer=writer)

# Display the animation
plt.show()