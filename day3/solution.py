# REGEX PART 1: pattern = r"mul\((\d+),(\d+)\)"

# REGEX PART 2: pattern = r"do\(\)|don't\(\)|mul\((\d+),(\d+)\)"


import re


nome_file = "input.txt"

with open(nome_file, "r") as file:
    input = file.read()

pattern = r"do\(\)|don't\(\)|mul\((\d+),(\d+)\)"

enabled = True
total_sum = 0

for match in re.finditer(pattern, input):
    if match.group() == "do()":
        enabled = True
    elif match.group() == "don't()":
        enabled = False
    elif enabled:
        x, y = map(int, match.groups())
        total_sum += x * y
    
print(total_sum)
