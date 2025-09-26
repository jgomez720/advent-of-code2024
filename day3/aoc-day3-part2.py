# day 3 part 2 advent of code 2024
# what is the total of all the multiplications of the enabled data?

import re

# create a function that calculates the total of the enabled portions in the corrupted dataset
def calculate_total(corrupted_data: str) -> int:

    # create a pattern that looks for mul(int, int), do(), and don't()
    pattern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"

    # create an iterable that is separated by the segments in the pattern
    tokens = re.finditer(pattern, corrupted_data)

    # the puzzle says to start with the data enabled
    enable = True

    # loop over each token, if it says do(), change enable to False, if it says don't, change enable to True. Otherwise, calculate the multiple inside the "mul()" segment. 
    counter = 0
    for m in tokens:
        if m.group().startswith("mul") and (enable):
            a, b = int(m.group(1)), int(m.group(2))
            counter += a * b

        elif m.group().startswith("do()"):
            enable = True

        elif m.group().startswith("don't()"):
            enable = False

    # return the count.
    return counter

# read data as one string
with open('day3.txt', 'r', encoding='utf-8') as f:
    data = f.read()

print(calculate_total(data))