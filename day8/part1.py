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
                x3, y3 = x1 - dx, y1 - dy
                x4, y4 = x2 + dx, y2 + dy
                
                if 0 <= x3 < map_shape[0] and 0 <= y3 < map_shape[1]:
                    antinodes.add((x3, y3))
                if 0 <= x4 < map_shape[0] and 0 <= y4 < map_shape[1]:
                    antinodes.add((x4, y4))
    
    return antinodes

def count_antinode_locations(file_path):
    map_array = parse_map(file_path)
    positions = find_antenna_positions(map_array)
    antinodes = calculate_antinodes(positions, map_array.shape)
    return len(antinodes)

file_path = "input.txt"

result = count_antinode_locations(file_path)
print(result)
