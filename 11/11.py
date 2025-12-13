
#!/usr/bin/python3

import sys

def part1(graph, key):
    total = 0
    for item in graph[key]:
        if item == "out":
            return 1
        else:
            total += part1(graph, item)
    return total

def part2(graph):
    total = count_paths(graph, 'svr', 'fft') * count_paths(graph, 'fft', 'dac') * count_paths(graph, 'dac', 'out')
    total += count_paths(graph, 'svr', 'dac') * count_paths(graph, 'dac', 'fft') * count_paths(graph, 'fft', 'out')
    return total

def count_paths(graph, start, end, memory=None):
    if memory is None:
        memory = {}
    if start == end:
        return 1
    if start in memory:
        return memory[start]
    if start == "out":
        return 0
    
    total = 0 
    for node in graph[start]:
        total += count_paths(graph, node, end, memory)
    memory[start] = total
    return total

graph = {}
filename = sys.argv[1] if len(sys.argv) > 1 else "11/example.txt"
with open(filename , "r") as f:
    for line in f:
        key, values = line.split(":")
        key = key.strip()
        values = values.strip().split()
        graph[key] = values
print("Part 1:", part1(graph, "you"))

graph = {}
filename = sys.argv[1] if len(sys.argv) > 1 else "11/example2.txt"
with open(filename , "r") as f:
    for line in f:
        key, values = line.split(":")
        key = key.strip()
        values = values.strip().split()
        graph[key] = values
print("Part 2:", part2(graph))