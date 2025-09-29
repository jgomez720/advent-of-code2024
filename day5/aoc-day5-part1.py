# Advent of Code 2024 Day 5 Part 1

def print_correct_pages(pages: list[str], rules: list[str]) -> list[str]:
    # for loop to check each line of the pages string

    # todo: need to compare each line in pages with every line in rules. If it passes ALL rules, then add the middle number of the pages. 
    sum = 0
    for line in pages:
        if all(line.index(rule[0]) < line.index(rule[1]) for rule in rules):
            sum += line[round(len(line)/2)] 
    
    return sum 

with open('example.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    rules, pages = data.split('\n\n')
    rules = rules.split('\n')

pages_array = [line.split(",") for line in pages.strip().splitlines()]
print(pages_array)

rules_pairs = []
    
# filter out the correct pairs. We only want strings that contain integers with three digits or less (not including zero)
for line in rules:
    print(line)
    a, b = line.split('|')
    rules_pairs.append((a, b)) # create ordered pairs of the rules

print(pages[0])
# print_correct_pages(pages, rules_pairs)