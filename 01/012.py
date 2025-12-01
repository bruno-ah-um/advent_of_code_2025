#!/usr/bin/env python3

import re
import sys

#starting position
pos = 50
last_pos = 50
times = 0

def split_code(code):
    m = re.match(r"([A-Z])(\d+)", code)
    return m.group(1), m.group(2)

#with open("01/example1.txt") as file:
with open("01/input1.txt") as file:
    while line := file.readline():
        direction, distance = split_code(line.strip())
        distance = int(distance)
        last_pos = pos
        times += distance // 100
        distance = distance % 100
        if direction == 'L':
            pos -= distance
            pos %= 100
            if pos == 0: 
                times += 1;
            if pos ==0 or last_pos == 0:
                continue
            if pos > last_pos:
                times += 1
        elif direction == 'R':
            pos += distance
            pos %= 100
            if pos == 0: 
                times += 1;
            if pos ==0 or last_pos == 0:
                continue
            if pos < last_pos:
                times += 1
        #if pos == 0:
        #    times+=1
    print(times)
    