import numpy as np
from itertools import product

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
    return result

def solve_equations(data):
    total = 0

    for row in data:
        test_value = row[0]
        numbers = row[1:]
        n = len(numbers)

        possible_operators = product(['+', '*'], repeat=n-1)

        for operators in possible_operators:
            if evaluate_expression(numbers, operators) == test_value:
                total += test_value
                break

    return total

def parse_input(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            test_value = int(parts[0])
            numbers = list(map(int, parts[1].split()))
            data.append([test_value] + numbers)
    return np.array(data, dtype=object)

input_file = "input.txt"
data = parse_input(input_file)

total = solve_equations(data)

print(total)
