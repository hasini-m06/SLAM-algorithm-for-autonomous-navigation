import numpy as np
import matplotlib.pyplot as plt

sensor_position = np.array([0.0, 0.0])
theta = np.radians(30)
local_point = np.array([3.0, 2.0])

R = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])

rotated_point = R @ local_point
global_point = sensor_position + rotated_point

print("Sensor position:", sensor_position)
print("Local point:", local_point)
print("Global point:", global_point)

plt.figure(figsize=(8, 8))

plt.xlim(-1, 6)
plt.ylim(-1, 6)

plt.xticks(range(7))
plt.yticks(range(7))

plt.grid(True)

plt.scatter(
    sensor_position[0],
    sensor_position[1],
    s=150,
    label="Sensor"
)

plt.scatter(
    global_point[0],
    global_point[1],
    s=150,
    label="Detected Object"
)

plt.plot(
    [sensor_position[0], global_point[0]],
    [sensor_position[1], global_point[1]],
    linestyle="--"
)

plt.xlabel("World X")
plt.ylabel("World Y")
plt.title("Grid-Based Spatial Mapping")
plt.legend()

plt.show()