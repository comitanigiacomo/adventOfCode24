# PART 1

import numpy as np
from collections import Counter

data = np.loadtxt('puzzleInput.txt', dtype=int)

left = np.sort(data[:, 0])
right = np.sort(data[:, 1])

total_sum = np.sum(np.abs(left - right))

print(total_sum)

# PART 2

frequency = Counter(right)

similarity = sum(elem * frequency[elem] for elem in left)

print(similarity)
