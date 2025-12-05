#!/usr/bin/python3

import sys

def part1(grid):
    times = 0
    for j in range(1, len(grid)-1):
        for i in range(1, len(grid[j])-1):
            count = 0
            if grid[j][i] == ".":
                continue
            for dj in [-1, 0, 1]:
                for di in [-1, 0, 1]:
                    if dj == 0 and di == 0:
                        continue
                    if grid[j+dj][i+di] != ".":
                        count += 1
            if count < 4:
                grid[j][i] = "x"
                times += 1
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            print(grid[j][i], end="")
        print()
    return times



def part2(grid):
    total = 0
    ret = part1(grid)
    while ret > 0:
        total += ret
        for j in range(1, len(grid)-1):
            for i in range(1, len(grid[j])-1):
                if grid[j][i] == "x":
                    grid[j][i] = "."
        ret = part1(grid)
    return total

filename = sys.argv[1]

grid = []
with open(filename) as f:
    for line in f:
        line = line.rstrip("\n")      # remove newline
        if line:                      # skip empty lines if any
            grid.append(list("." + line + "."))   # prepend + append dots

# Width after padding each line
width = len(grid[0])

# Add a top and bottom padding line
padding_row = ["." for _ in range(width)]
grid.insert(0, padding_row)
grid.append(padding_row[:])  # copy

# Example: print the grid
for row in grid:
    print(row)

print("Part 1:", part1(grid))
print("Part 2:", part2(grid))