import numpy as np

def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        lines = [list(line.strip()) for line in file.readlines()]
    return np.array(lines)

def find_xmas_in_x_shape(matrix):
    rows, cols = matrix.shape
    total_xmas = 0

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if matrix[i, j] == 'A':
                if (
                    (matrix[i-1, j-1] == 'M' and matrix[i+1, j+1] == 'S') or
                    (matrix[i-1, j-1] == 'S' and matrix[i+1, j+1] == 'M')
                ) and (
                    (matrix[i-1, j+1] == 'M' and matrix[i+1, j-1] == 'S') or
                    (matrix[i-1, j+1] == 'S' and matrix[i+1, j-1] == 'M')
                ):
                    total_xmas += 1

    return total_xmas


matrix = read_matrix_from_file("input.txt")

total_xmas = find_xmas_in_x_shape(matrix)

print(total_xmas)
