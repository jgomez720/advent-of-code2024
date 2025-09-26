# Day 1, Part 2 of Advent of Code 2024
# What is the similarity score between your lists?

# Create a function that calculates the total difference between all numbers in two lists. 
def calculate_simularity(list1: list[int], list2: list[int]) -> int:
    # Sort the lists numerically
    list1_sorted = sorted(list1)
    list2_sorted = sorted(list2)

    # Number by number, calculate the difference between the two arrays. Add up the differences.
    total = 0
    for i in range(len(list1_sorted)):
        total += list1_sorted[i] * list2_sorted.count(list1_sorted[i])

    return total

# Create two empty arrays.
list1 = []
list2 = []

# Read the file and split the lines into two arrays.
with open('day1.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if line.strip():
            a, b = line.split()
            list1.append(int(a))
            list2.append(int(b))

print(calculate_simularity(list1, list2))