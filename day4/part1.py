import numpy as np

def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        lines = [list(line.strip()) for line in file.readlines()]
    return np.array(lines)

def extract_lines_and_diagonals(matrix):
    rows, cols = matrix.shape
    lines = []

    for row in matrix:
        lines.append("".join(row))
        lines.append("".join(row[::-1]))


    for col in range(cols):
        col_str = "".join(matrix[:, col])
        lines.append(col_str)
        lines.append(col_str[::-1])

    for offset in range(-rows + 1, cols):
        diag = matrix.diagonal(offset)
        lines.append("".join(diag))
        lines.append("".join(diag[::-1]))

        flipped_matrix = np.fliplr(matrix)
        flipped_diag = flipped_matrix.diagonal(offset)
        lines.append("".join(flipped_diag))
        lines.append("".join(flipped_diag[::-1]))

    return lines

matrix = read_matrix_from_file("input.txt")
total_xmas = 0

all_lines = extract_lines_and_diagonals(matrix)

for line in all_lines:
    total_xmas += line.count("XMAS")   
         
print(total_xmas)
