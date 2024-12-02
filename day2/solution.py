from collections import Counter


nome_file = "input.txt"

with open(nome_file, "r") as file:
    righe = file.readlines()

array_di_interi = [list(map(int, riga.split())) for riga in righe]

total_safe = 0
total_semi_safe = 0

def is_safe(riga: list[int]) -> bool:
    differences = [abs(riga[i] - riga[i - 1]) for i in range(1, len(riga))]
               
    is_increasing = all(riga[i] >= riga[i - 1] for i in range(1, len(riga)))
    is_decreasing = all(riga[i] <= riga[i - 1] for i in range(1, len(riga)))
    valid_differences = all(1 <= diff <= 3 for diff in differences)
    
    if valid_differences and (is_decreasing or is_increasing): 
        return True
    
    return False

for riga in array_di_interi:
    if is_safe(riga): 
        total_safe += 1
    else:
        for problem in range(len(riga)):
            if is_safe(riga[:problem] + riga[problem+1:]):
                total_semi_safe += 1
                break

print(total_safe)
print(total_safe + total_semi_safe)
