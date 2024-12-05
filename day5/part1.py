import numpy as np
from collections import defaultdict

filename = "input.txt"

with open(filename, "r") as file:
    file_content = file.read()

part1, part2 = file_content.split("\n\n")

data = np.loadtxt(part1.splitlines(), delimiter="|", dtype=int)

mapping = defaultdict(list)
for key, value in data:
    mapping[key].append(value)

arrays = [list(map(int, row.split(","))) for row in part2.splitlines()]

is_valid = True

total_sum = 0

for arr in arrays:
    is_valid = True
    for i in range(1, len(arr)):
        for elem in mapping[arr[i]]:
            if elem in arr[:i]:
                is_valid = False
                break
        if not is_valid: break
    if is_valid:
        total_sum += arr[len(arr)//2]
    
print(total_sum)
