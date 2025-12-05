#!/usr/bin/python3

import numbers
import sys
from itertools import combinations

def part1(arrays):
    total = 0
    for array in arrays:
        max1 = 0
        for i in range(len(array) - 1):
            if array[i] > array[max1]:
                max1 = i
        max2 = max1+1
        for i in range(max2+1, len(array)):
            if array[i] > array[max2]:
                max2 = i
        number = int(str(array[max1]) + str(array[max2]))
        total += number
    return total

def find_next_greater(array, start_index, len):
    max = array[start_index]
    max_i = start_index
    for i in range(start_index+1, len):
        if array[i] > max:
            max = array[i]
            max_i = i
    return max_i

def part2(arrays):
    total = 0
    for array in arrays:
        max_i = 0
        result = ""
        for i in range(12):
            max_i = find_next_greater(array, max_i, len(array)-11+i)
            result = result + str(array[max_i])
            max_i += 1
        total += int(result)    
    return total

filename = sys.argv[1]
with open(filename) as f:
    arrays = [list(map(int, line.strip())) for line in f if line.strip()]

print("Part 1:", part1(arrays))
print("Part 2:", part2(arrays))