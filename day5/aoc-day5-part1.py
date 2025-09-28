# Advent of Code 2024 Day 5 Part 1

def print_correct_pages(pages: list[str], rules: list[str]) -> list[str]:
    # for loop to check each line of the pages string

    
    return

with open('example.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    rules, pages = data.split('\n\n')
    rules = rules.split('\n')
    pages = pages.split('\n')

print(rules)
print(pages)

rules_pairs = []
    
# filter out the correct pairs. We only want strings that contain integers with three digits or less (not including zero)
for line in rules:
    print(line)
    a, b = line.split('|')
    rules_pairs.append((a, b))

print(rules_pairs)