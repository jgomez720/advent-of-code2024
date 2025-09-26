# Day 2, Part 2 of Advent of Code 2024
# How many reports are safe with the dampener?

# Define a function that calculates whether the report is safe or not (same as part 1). 
def is_safe(levels: list[int]) -> bool:

    # Create an array that displays the diffs between each number. 
    diffs = [b - a for a, b in zip(levels, levels[1:])]
    
    if not diffs:  # check for levels that have 0 or 1 entries. 
        return False 
    
    # strictly increasing
    inc_ok = all(1 <= d <= 3 for d in diffs)
    
    # strictly decreasing
    dec_ok = all(-3 <= d <= -1 for d in diffs)
    return inc_ok or dec_ok

# Define another function that calculates whether the report is safe with the dampener. 
def is_safe_with_dampener(levels: list[int]) -> bool:
    if is_safe(levels): # If it's already safe, return True
        return True
    
    # If it's not, create a new list called "candidate" that takes everything before and after i. Run is_safe() on that list. If it's safe, return True, else return False. 
    for i in range(len(levels)):
        candidate = levels[:i] + levels[i+1:]
        if is_safe(candidate):
            return True
    return False

# Create an empty array.
nested_array = []

# Read the file and split the lines into a nested array. 
with open('day2.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if line.strip():
            row = [int(num) for num in line.split()]
            nested_array.append(row)

# calculate the sum. True evaluates to 1, False evaluates to 0, which is why we can use sum on a list of booleans. 
counter = sum(is_safe_with_dampener(row) for row in nested_array)
print(counter)