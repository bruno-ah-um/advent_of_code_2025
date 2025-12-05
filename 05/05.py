#!/usr/bin/python3

import sys

def part1(fresh_pairs, ingredients):
    count = 0
    for ingredient in ingredients:
        for a, b in fresh_pairs:
            if a <= ingredient and b >= ingredient:
                count += 1
                break
    return count

def part2(fresh_pairs):
    total = 0
    processed_pairs = []
    for a, b in fresh_pairs:
        ignore = False
        for a2, b2 in processed_pairs:
            if (a < a2 and b < a2) or (a > b2 and b > b2):
                # Do not overlap
                continue
            else:
                if a >= a2 and b <= b2:
                    ignore = True
                    continue
                elif a < a2 and b <= b2:
                    b = a2 -1
                    continue
                elif a >= a2 and b > b2:
                    a = b2 +1
                    continue
                else:
                    fresh_pairs.append((a, a2-1))
                    fresh_pairs.append((b2 +1, b))
                    ignore = True
                    break
                    
                    
        if not ignore:
            processed_pairs.append((a,b))

    for a, b in processed_pairs:
        total += (b - a + 1)

    return total

filename = sys.argv[1]

reached_empty_line = False
fresh_pairs = []
ingredients = []

with open(filename) as f:
    for raw_line in f:
        line = raw_line.strip()
        if not reached_empty_line:
            if line == "":
                reached_empty_line = True
            else:
                a, b = map(int, line.split("-"))
                fresh_pairs.append((a, b))
            continue
        else:
            # --- SECOND PART: lines after the empty line ---
            ingredients.append(int(line))

print("Part 1:", part1(fresh_pairs, ingredients))
print("Part 2:", part2(fresh_pairs))