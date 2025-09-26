# day 4 part 2 Advent of Code 2024
# Find all the X-"MAS" in the word search

# Create a function that takes in a large string of data and outupts the amount of times "XMAS" is found
def find_xmas(grid: str) -> int:
    
    # Define the rows and the columns of the grid
    rows, cols = len(grid), len(grid[0])

    counter = 0

    # Loop through each character, once we land on an "A", go through each case and add to the counter if the case succeeds. 
    for r in range(rows):
        for c in range(cols):

            if grid[r][c] == "A" and r > 0 and r < len(grid)-1 and c > 0 and c < len(grid[r]) - 1: # We are only going to check if we are on an "A" (it must be the center of the X). Added boundary conditions to ensure we aren't checking A's that are on the perimeter. 
            
                ## CASE 1: M's are in top left and top right
                if grid[r-1][c-1] == "M" and grid[r-1][c+1] == "M":
                    if grid[r+1][c-1] == "S" and grid[r+1][c+1] == "S":
                        counter += 1

                ## CASE 2: M's are in top left and bottom left
                if grid[r-1][c-1] == "M" and grid[r+1][c-1] == "M":
                    if grid[r-1][c+1] == "S" and grid[r+1][c+1] == "S":
                        counter += 1

                ## CASE 3: M's are in top right and bottom right
                if grid[r-1][c+1] == "M" and grid[r+1][c+1] == "M":
                    if grid[r-1][c-1] == "S" and grid[r+1][c-1] == "S":
                        counter += 1

                ## CASE 4: M's are in bottom left and bottom right
                if grid[r+1][c-1] == "M" and grid[r+1][c+1] == "M":
                    if grid[r-1][c-1] == "S" and grid[r-1][c+1] == "S":
                        counter += 1

            else:
                continue
    return counter

with open('day4.txt', 'r', encoding='utf-8') as f:
    data = [line.strip() for line in f.readlines()]

## Answer
print(find_xmas(data))