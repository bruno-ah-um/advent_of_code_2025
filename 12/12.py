
#!/usr/bin/python3

import sys
from typing import List, Tuple

def count_ones(piece):
    return sum(sum(row) for row in piece)

def part1(pieces, tiles ,problems):
    fit = 0
    for p in problems:
        area = p[0] * p[1]

        # Enough space for all presents
        easy_area = (p[0] //3) * (p[1] // 3)
        needed = sum(int(x) for x in p[2])
        if needed <= easy_area:
            fit += 1
            continue
        
        # Calculate the number of tiles
        num_tiles_min = sum(
            t * quantity
            for t, quantity in zip(tiles, p[2])
        )
        if num_tiles_min > area:
            continue

        print("too complicated")

    return fit

def part2():
    return 0

def parse_file(text: str):
    lines = [line.rstrip() for line in text.splitlines()]

    pieces: List[List[List[int]]] = []
    problems: List[Tuple[int, int, List[int]]] = []

    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]

        if not line:
            i += 1
            continue

        if "x" in line and ":" in line:
            break

        if line.endswith(":"):
            i += 1
            matrix = []

            while i < n and lines[i] and not lines[i].endswith(":"):
                row = [1 if c == "#" else 0 for c in lines[i]]
                matrix.append(row)
                i += 1
            pieces.append(matrix)
        else:
            i += 1
    while i < n:
        line = lines[i]
        i += 1

        if not line:
            continue

        # Example: "12x5: 1 0 1 0 2 2"
        size_part, indices_part = line.split(":")
        width, height = map(int, size_part.split("x"))
        indices = list(map(int, indices_part.split()))

        problems.append((width, height, indices))

    return pieces, problems


graph = {}
filename = sys.argv[1] if len(sys.argv) > 1 else "12/input.txt"
with open(filename) as f:
    text = f.read()

pieces, problems = parse_file(text)

print("Pieces:")
for p in pieces:
    print(p)

tiles = []
for p in pieces:
    tiles.append(count_ones(p))

print("Tiles:")
for t in tiles:
    print(t)

print("\nProblems:")
for prob in problems:
    print(prob)

print("Part 1:", part1(pieces, tiles, problems))
print("Part 2:", part2())