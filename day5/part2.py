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

def order_array(arr):
    n = len(arr)
    is_sorted = False
    swaps_made = False

    while not is_sorted:
        is_sorted = True
        for i in range(1, n):
            for elem in mapping[arr[i]]:
                if elem == arr[i-1]:
                    arr[i-1], arr[i] = arr[i], arr[i-1]
                    is_sorted = False
                    swaps_made = True
                    break
            if not is_sorted:
                break

    return arr, swaps_made

total_sum = 0
for arr in arrays:
    sorted_arr, swaps_made = order_array(arr)
    if swaps_made:
        total_sum += sorted_arr[len(sorted_arr) // 2]

print(total_sum)
