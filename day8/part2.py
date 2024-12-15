import numpy as np

def parse_map(file_path):
    with open(file_path, 'r') as f:
        lines = f.read().strip().split("\n")
    return np.array([list(line) for line in lines])

def find_antenna_positions(map_array):
    positions = {}
    for (x, y), value in np.ndenumerate(map_array):
        if value != '.':
            positions.setdefault(value, []).append((x, y))
    return positions

def calculate_antinodes(positions, map_shape):
    antinodes = set()

    for coords in positions.values():
        n = len(coords)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = coords[i]
                x2, y2 = coords[j]

                dx, dy = x2 - x1, y2 - y1

                gcd = np.gcd(dx, dy)
                dx //= gcd
                dy //= gcd

                k = 0
                while True:
                    nx, ny = x1 + k * dx, y1 + k * dy
                    if 0 <= nx < map_shape[0] and 0 <= ny < map_shape[1]:
                        antinodes.add((nx, ny))
                    else:
                        break
                    k += 1

                k = -1
                while True:
                    nx, ny = x1 + k * dx, y1 + k * dy
                    if 0 <= nx < map_shape[0] and 0 <= ny < map_shape[1]:
                        antinodes.add((nx, ny))
                    else:
                        break
                    k -= 1

    return len(antinodes)

def count_antinode_locations(file_path):
    map_array = parse_map(file_path)
    positions = find_antenna_positions(map_array)
    antinode_count = calculate_antinodes(positions, map_array.shape)
    return antinode_count

file_path = "input.txt"
result = count_antinode_locations(file_path)
print(result)
