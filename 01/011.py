#!/usr/bin/env python3

import re
import sys

#starting position
pos = 50
times = 0

def split_code(code):
    m = re.match(r"([A-Z])(\d+)", code)
    return m.group(1), m.group(2)

for line in sys.stdin.readlines():
    direction, distance = split_code(line.strip())
    if direction == 'L':
        pos -= int(distance)
    elif direction == 'R':
        pos += int(distance)
    pos %= 100
    if pos == 0:
        times+=1
print(times)
    