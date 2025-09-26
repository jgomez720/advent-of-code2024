# day 3 part 1 advent of code 2024
# what is the total of all the multiplications in the corrupted data?

import re # regex

# create function to find "mul(int, int)"
def find_mull(corrupted_data: str) -> list[str]:

    matches = re.findall(r"mul\((\d+),(\d+)\)", corrupted_data) # finsd "mul(" + digit + "," + digit + ")"
    return matches

# read data as one string
with open('day3.txt', 'r', encoding='utf-8') as f:
    data = f.read()

def calculate_total(input: list[str]) -> int:
    pairs = []
    
    # filter out the correct pairs. We only want strings that contain integers with three digits or less (not including zero)
    for a, b in input:
        a, b = int(a), int(b)
        if 0 < a < 1000 and 0 < b < 1000:
            pairs.append((a, b))
    
    result = sum(a * b for a, b in pairs)
    return result

# find mul strings in the data
uncorrupted_data = find_mull(data)
total = calculate_total(uncorrupted_data)

print(total)