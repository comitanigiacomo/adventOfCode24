from collections import defaultdict
import numpy as np

def split_number(num):
    num_str = str(num)
    mid = len(num_str) // 2
    left = int(num_str[:mid]) if num_str[:mid] else 0
    right = int(num_str[mid:]) if num_str[mid:] else 0
    return left, right

def transform_stones_map(stones_map):
    new_stones_map = defaultdict(int)
    for stone, count in stones_map.items():
        if stone == 0:
            new_stones_map[1] += count
        elif len(str(stone)) % 2 == 0:
            left, right = split_number(stone)
            new_stones_map[left] += count
            new_stones_map[right] += count
        else:
            new_stones_map[stone * 2024] += count
    return new_stones_map

def simulate_blinks_map(initial_stones, num_blinks):
    stones_map = defaultdict(int)
    for stone in initial_stones:
        stones_map[stone] += 1

    for _ in range(num_blinks):
        stones_map = transform_stones_map(stones_map)

    return stones_map

filename = "input.txt"
initial_stones = np.loadtxt(filename, dtype=int).tolist()

final_stones_map = simulate_blinks_map(initial_stones, 75)

total_stones = sum(final_stones_map.values())
print(total_stones)
