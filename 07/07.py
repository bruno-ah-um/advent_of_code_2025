#!/usr/bin/python3

import sys
from functools import cache

times = 0

def part1(grid):
    count = 0
    for i in range(len(grid)-1):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                grid[i+1][j] = '|'
            if grid[i][j] == '|' and  grid[i+1][j] == '.':
                grid[i+1][j] = '|'
            if grid[i][j] == '|' and  grid[i+1][j] == '^':
                count += 1
                if j > 0:
                    grid[i+2][j-1] = '|'
                if j < (len(grid[i])-1):
                    grid[i+2][j+1] = '|'

    #for i in range(len(grid)):
    #   print(grid[i])
    return count

def part2(lines):
    splitter_rows = [line for line in lines if "^" in line]

    @cache
    def dfs(x, c):
        if x == len(splitter_rows):
            return 1
        if not (0 <= c < len(lines[0])):
            return 0
        if splitter_rows[x][c] == "^":
            return dfs(x + 1, c - 1) + dfs(x + 1, c + 1)
        return dfs(x + 1, c)

    return dfs(0, lines[0].index("S"))

filename = sys.argv[1]
with open(filename, "r") as f:
    grid = [list(line.rstrip("\n")) for line in f]

grid_copy = [row[:] for row in grid]
print("Part 1:", part1(grid_copy))
lines = open(filename).read().splitlines()
print("Part 2:", part2(lines))