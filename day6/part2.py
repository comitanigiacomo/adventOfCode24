import numpy as np

def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        lines = [list(line.strip()) for line in file.readlines()]
    return np.array(lines)

def simulate_with_obstruction(matrix, obs_x, obs_y, start_x, start_y):
    rows, cols = matrix.shape
    directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    idx_direction = 0
    visited = set()
    
    matrix[obs_y][obs_x] = '#'
    
    curr_x, curr_y = start_x, start_y
    while 0 <= curr_x < cols and 0 <= curr_y < rows:
        state = (curr_x, curr_y, idx_direction)
        if state in visited:
            
            matrix[obs_y][obs_x] = '.'
            return True
        visited.add(state)

        next_x, next_y = curr_x + directions[idx_direction][0], curr_y + directions[idx_direction][1]
        if 0 <= next_x < cols and 0 <= next_y < rows and matrix[next_y][next_x] == '#':
            idx_direction = (idx_direction + 1) % len(directions)
        else:
            curr_x, curr_y = next_x, next_y
    
    matrix[obs_y][obs_x] = '.'
    return False

def find_obstruction_positions(filename):
    matrix = read_matrix_from_file(filename)
    rows, cols = matrix.shape

    start_x, start_y = 0, 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '^':
                start_x, start_y = j, i
                break

    valid_positions = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '.' and (j != start_x or i != start_y):
                if simulate_with_obstruction(matrix, j, i, start_x, start_y):
                    valid_positions += 1

    return valid_positions

filename = "input.txt"
result = find_obstruction_positions(filename)
print(result)
