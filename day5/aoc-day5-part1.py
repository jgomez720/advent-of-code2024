# Advent of Code 2024 Day 5 Part 1

def sum_center_number_of_correct_pages(pages: list[str], rules: list[str]) -> list[str]:
    # for loop to check each line of the pages string

    total = 0

    for line in pages:
        pos = {val: i for i, val in enumerate(line)} 

        if all(pos[a] < pos[b] for a, b in rules if a in pos and b in pos):
            total += int(line[len(line) // 2])  # middle value

    return total

with open('day5.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    rules, pages = data.split('\n\n')
    rules = rules.split('\n')

pages_array = [line.split(",") for line in pages.strip().splitlines()]
rules_pairs = []
    
# filter out the correct pairs. We only want strings that contain integers with three digits or less (not including zero)
for line in rules:
    a, b = line.split('|')
    rules_pairs.append((a, b)) # create ordered pairs of the rules

print(sum_center_number_of_correct_pages(pages_array, rules_pairs))