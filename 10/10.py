
#!/usr/bin/python3

import sys
import re
from itertools import combinations
from z3 import Int, Optimize, sat

def part2(input):
    total = 0
    for line in input:
        results = []

        solution = line['set']
        buttons = line['tuples']
        num_vars = len(buttons)

        vars = [Int(f'x{i}') for i in range(num_vars)]

        equations = []
        for i in range(len(solution)):
            v = []
            for j in range(len(buttons)):
                button = buttons[j]
                if i in button:
                    v.append(j)
            equations.append((v,solution[i]))

        opt = Optimize()

        for indices, rhs in equations:
            opt.add(sum(vars[i] for i in indices) == rhs)

        # Solutions equal or bigger than 0
        opt.add([v >= 0 for v in vars])

        # Minimize sum
        opt.minimize(sum(vars))

        # Solve
        if opt.check() == sat:
            model = opt.model()
            solution = [model[v].as_long() for v in vars]
            print("Optimal solution:", solution)
            print("Minimum sum:", sum(solution))
            total += sum(solution)
        else:
            print("No solution found")

    return total


def calculate(combo, pattern):
    result = ['.'] * len(pattern)
    for tup in combo:
        for idx in tup:
            if idx < 0 or idx >= len(result):
                continue  # skip invalid indices
            result[idx] = '#' if result[idx] == '.' else '.'
    result_str = ''.join(result)
    return result_str == pattern

def all_tuple_combinations(tuples):
    results = []
    n = len(tuples)
    for r in range(1, n+1):     # choose 1 to n tuples
        for combo in combinations(tuples, r):
            results.append(combo)
    return results

def part1(input):
    total = 0
    for line in input:
        results = []
        all_combos = all_tuple_combinations(line["tuples"])
        
        for combo in all_combos:
            result = calculate(combo, line["pattern"])
            results.append((result, combo))
        true_results = [(res, combo) for res, combo in results if res]
        if true_results:
            min_length = min(len(combo) for _, combo in true_results)
            total += min_length
        else:
            print("ERROR")

    return total

def parse_line(line):
    # Extract the bracket pattern: [.##.]
    pattern = re.search(r'\[(.*?)\]', line).group(1)
    
    # Extract all tuples: (3), (1,3), ...
    tuples = [
        tuple(map(int, t.split(',')))
        for t in re.findall(r'\((.*?)\)', line)
    ]
    
    # Extract set: {3,5,4,7}
    set_match = re.search(r'\{(.*?)\}', line)
    
    values_list = ([int(x.strip()) for x in set_match.group(1).split(',')] if set_match else None )

    return {
        "pattern": pattern,
        "tuples": tuples,
        "set": values_list
    }

input = []
filename = sys.argv[1] if len(sys.argv) > 1 else "10/example.txt"
with open(filename , "r") as f:
    for line in f:
        line = line.strip()
        if line:
            input.append(parse_line(line))


print("Part 1:", part1(input))
print("Part 2:", part2(input))