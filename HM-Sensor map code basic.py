import numpy as np

map_size = 10
main_map = np.zeros((map_size, map_size), dtype=int)

sensor_x = 2
sensor_y = 2
sensor_spot = np.array([sensor_x, sensor_y])

main_map[sensor_y, sensor_x] = 8

seen_items = np.array([
    [3, 4],   
    [1, 2],   
    [5, 1],   
    [2, -4]   
])

real_spots = sensor_spot + seen_items

for item in real_spots:
    item_x = item[0]
    item_y = item[1]

    if 0 <= item_x < map_size and 0 <= item_y < map_size:
        main_map[item_y, item_x] = 1  # 1 means item found
    else:
        print(f"Point ({item_x}, {item_y}) is off the map!")

print("\n--- FINAL MAP ---")
print("8 = Sensor, 1 = Found Item, 0 = Empty Spot\n")

print(np.flipud(main_map))