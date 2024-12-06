import numpy as np

def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        lines = [list(line.strip()) for line in file.readlines()]
    return np.array(lines)

matrix = read_matrix_from_file("input.txt")
total_steps = 0
curr_x, curr_y = 0, 0

directions = [[0, -1], [1, 0], [0, +1], [-1, 0]]
direction = directions[0]
idx_direction = 0
visited = []

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == '^':
            curr_x = j
            curr_y = i
            break

while (0 <= curr_x < len(matrix)) and (0 <= curr_y < len(matrix[0])):
    tmp_x, tmp_y = curr_x + direction[0], curr_y + direction[1]
    if (tmp_x >= len(matrix)) or (tmp_y < 0 or tmp_y >= len(matrix[0])):
        break

    if matrix[tmp_y][tmp_x] == '#':
        idx_direction = (idx_direction + 1) % len(directions)
        direction = directions[idx_direction]
    else:
        curr_x, curr_y = tmp_x, tmp_y
        if [curr_x, curr_y] not in visited:
            total_steps += 1
            visited.append([curr_x, curr_y])

print(total_steps + 1)