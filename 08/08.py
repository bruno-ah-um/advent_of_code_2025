#!/usr/bin/python3

import sys
import math

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)

def is_in_matched(p1, p2, matched_pairs):
    for pair in matched_pairs:
        if (p1, p2) == pair or (p2, p1) == pair:
            return True
    return False

groups = []

def add_to_groups(p1, p2):
    global groups
    group_p1 = -1
    group_p2 = -1
    for i in range(len(groups)):
        group = groups[i]
        if p2 in group and p1 in group:
            return False
        if p2 in group and not p1 in group:
            group_p2 = i
        if p1 in group and not p2 in group:
            group_p1 = i
            #group.append(p2)

    if group_p1 == -1 and group_p2 == -1:
        e = [p1, p2]
        groups.append(e)
        return True
    
    if group_p1 == -1:
        groups[group_p2].append(p1)
    
    if group_p2 == -1:
        groups[group_p1].append(p2)

    if group_p1 != -1 and group_p2 != -1:
        for g in groups[group_p2]:
            groups[group_p1].append(g)
        del groups[group_p2]

    return True

def part1(coordinates, times):
    global groups
    
    matched_pairs = []
    closest_pair = None
    counter = 0

    while counter < times:
        print(counter)
        min_dist = float('inf')
        # Iterate over all pairs
        for i in range(len(coordinates)):
            for j in range(i+1, len(coordinates)):
                d = distance(coordinates[i], coordinates[j])
                if d < min_dist:
                    if not is_in_matched(coordinates[i], coordinates[j], matched_pairs):
                        min_dist = d
                        closest_pair = (coordinates[i], coordinates[j])

        #print(closest_pair)
        matched_pairs.append(closest_pair)
        if add_to_groups(closest_pair[0], closest_pair[1]):
            counter += 1
        else:
            counter += 1

        
        lengths = [len(group) for group in groups]
        total_length = sum(lengths)
        print("Groups: " +  str(len(groups)) + " l " + str(total_length))
    
    lengths = [len(group) for group in groups]
    sorted_lengths = sorted(lengths, reverse=True)
    print(sorted_lengths)
    total = sorted_lengths[0] * sorted_lengths[1] *sorted_lengths[2]
    print(total)
    
    return total

def part1(coordinates):
    global groups
    
    matched_pairs = []
    closest_pair = None
    counter = 0
    flag = True

    while flag:
        print(counter)
        min_dist = float('inf')
        # Iterate over all pairs
        for i in range(len(coordinates)):
            for j in range(i+1, len(coordinates)):
                d = distance(coordinates[i], coordinates[j])
                if d < min_dist:
                    if not is_in_matched(coordinates[i], coordinates[j], matched_pairs):
                        min_dist = d
                        closest_pair = (coordinates[i], coordinates[j])

        #print(closest_pair)
        matched_pairs.append(closest_pair)
        if add_to_groups(closest_pair[0], closest_pair[1]):
            counter += 1
        else:
            counter += 1

        lengths = [len(group) for group in groups]
        total_length = sum(lengths)
        print("Groups: " +  str(len(groups)) + " l " + str(total_length))
        if len(groups) == 1 and total_length == len(coordinates):
            flag = False
        
    print("last couple_ ")
    print(closest_pair)

    return closest_pair[0][0] * closest_pair[1][0]

filename = sys.argv[1]
coordinates = []

with open(filename , "r") as f:
    for line in f:
        x, y, z = map(int, line.strip().split(','))
        coordinates.append((x, y, z))

print(coordinates)
#print("Part 1:", part1(coordinates, 1000))
print("Part 2:", part1(coordinates))