# day 4 part 1 Advent of Code 2024
# Find all the "XMAS" in the word search

# Create a function that takes in a large string of data and outupts the amount of times "XMAS" is found
def find_xmas(grid: str) -> int:
    
    # Define the rows and the columns of the grid
    rows, cols = len(grid), len(grid[0])

    counter = 0

    # Loop through each character, once we land on an "X", go through each case and add to the counter if the case succeeds. 
    for r in range(rows):
        for c in range(cols):

            if grid[r][c] == "X": # We only need to test cases if we are currently on a "X"
               
                ## HORIZONTAL FORWARD ##
                if c < len(grid[r]) - 3:
                    if grid[r][c:c+4] == "XMAS":
                        counter += 1

                ## HORIZONTAL BACKWARD ##
                if c > 2:
                    if grid[r][c-3:c+1] == "SAMX":
                        counter += 1

                ## VERTICAL UP ##
                if r > 2:
                    if grid[r-1][c] == "M":
                        if grid[r-2][c] == "A":
                            if grid[r-3][c] == "S":
                                counter += 1

                ## VERTICAL DOWN ##
                if r < len(grid)-3:
                    if grid[r+1][c] == "M":
                        if grid[r+2][c] == "A":
                            if grid[r+3][c] == "S":
                                counter += 1

                ## DIAGONAL UP-RIGHT ##
                if r > 2 and c < len(grid[r]) - 3:
                    if grid[r-1][c+1] == "M":
                        if grid[r-2][c+2] == "A":
                            if grid[r-3][c+3] == "S":
                                counter += 1

                ## DIAGONAL UP-LEFT ##
                if r > 2 and c > 2:
                    if grid[r-1][c-1] == "M":
                        if grid[r-2][c-2] == "A":
                            if grid[r-3][c-3] == "S":
                                counter += 1

                ## DIAGONAL DOWN-LEFT ##
                if r < len(grid)-3 and c > 2:
                    if grid[r+1][c-1] == "M":
                        if grid[r+2][c-2] == "A":
                            if grid[r+3][c-3] == "S":
                                counter += 1

                ## DIAGONAL DOWN-RIGHT ##
                if r < len(grid)-3 and c < len(grid[0])-3:
                    if grid[r+1][c+1] == "M":
                        if grid[r+2][c+2] == "A":
                            if grid[r+3][c+3] == "S":
                                counter += 1
            else:
                continue
    return counter

with open('day4.txt', 'r', encoding='utf-8') as f:
    data = [line.strip() for line in f.readlines()]

## Answer
print(find_xmas(data))