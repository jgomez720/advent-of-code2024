# Day 2, Part 1 of Advent of Code 2024
# How many reports are safe?

# Define a function that calculates whether the level is safe or not. 
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



# Create an empty array.
nested_array = []

# Read the file and split the lines into a nested array. 
with open('day2.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if line.strip():
            row = [int(num) for num in line.split()]
            nested_array.append(row)

# calculate the sum. True evaluates to 1, False evaluates to 0, which is why we can use sum on a list of booleans. 
counter = sum(is_safe(row) for row in nested_array)
print(counter)