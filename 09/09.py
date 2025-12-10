#!/usr/bin/python3

import sys

def area(p1, p2):
    return (abs(p1[0]-p2[0])+1) * (abs(p1[1]-p2[1])+1)

def part1(coordinates):
    max = 0
    for i in range(len(coordinates)):
        for j in range(i+1, len(coordinates)):
            a = area(coordinates[i],coordinates[j])
            if (a > max):
                max = a
    return max

def part2(coordinates):
    n = len(coordinates)

    def get_size(x1, y1, x2, y2):
        x = abs(x1 - x2) + 1
        y = abs(y1 - y2) + 1
        return x * y

    edges = []
    sizes = []
    for i in range(n):
        edges.append(sorted((coordinates[i], coordinates[i-1])))
        for j in range(i+1, n):
            c1, c2 = sorted((coordinates[i], coordinates[j]))
            sizes.append((get_size(*c1, *c2), c1, c2))

    edges.sort(reverse=True, key=lambda e: get_size(*e[0], *e[1]))
    sizes.sort(reverse=True)

    for size, (x1, y1), (x2, y2) in sizes:
        y1, y2 = sorted((y1, y2))
        if not any(
            (x4 > x1 and x3 < x2 and y4 > y1 and y3 < y2)
            for (x3, y3), (x4, y4) in edges
        ):
            return size

filename = sys.argv[1] if len(sys.argv) > 1 else "09/example.txt"
coordinates = []

with open(filename , "r") as f:
    for line in f:
        x, y = map(int, line.strip().split(','))
        coordinates.append((x, y))

print(coordinates)
col1, col2 = zip(*coordinates)

# Compute min and max
min_col1, max_col1 = min(col1), max(col1)
min_col2, max_col2 = min(col2), max(col2)

data = tuple(coordinates)
print("Part 1:", part1(data))
print("Part 2:", part2(data))