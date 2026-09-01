import numpy as np
import matplotlib.pyplot as plt

sensor_position = np.array([0.0, 0.0])
theta = np.radians(30)

local_point = np.array([3.0, 2.0])

R = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])

global_point = sensor_position + R @ local_point

print("Sensor position:", sensor_position)
print("Sensor orientation:", np.degrees(theta), "degrees")
print("Local reading:", local_point)
print("Global position:", global_point)

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

plt.arrow(
    0,
    0,
    2 * np.cos(theta),
    2 * np.sin(theta),
    head_width=0.15,
    length_includes_head=True
)

plt.xlabel("World X")
plt.ylabel("World Y")
plt.title("Spatial Mapping with Sensor Orientation")

plt.legend()
plt.show()