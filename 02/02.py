#!/usr/bin/env python3

from unittest import result

def divisors(n):
    result = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            result.add(i)
            result.add(n // i)
    return sorted(result)

def iswrong2(number):
    
    divs = divisors(len(number))
    for div in divs:

        if len(number) == div:
            continue

        first = number[:div]
        i = div
        is_wrong = True
        while(i+div <= len(number)):
            next = number[i:i+div]
            if first != next:
                is_wrong = False
                break
            i += div
        if is_wrong:
            return True
    return False

def iswrong(number):
    if len(number) % 2 != 0:
        return False
    half = len(number) // 2
    return number[:half] == number[half:]

def add_invalid(inputs, checker):
    total = 0
    for input in inputs:
        for number in range(input[0], input[1] + 1):
            if checker(str(number)):
                total += number
    return total

with open("02/input.txt", "r") as f:
    data = f.read()

clean = data.replace("\n", "").strip(",")
pairs = clean.split(",")

inputs = list(
    map(lambda x: tuple(map(int, x.split("-"))), pairs)
)

#print(inputs)

print("Part 1:", add_invalid(inputs, iswrong))
print("Part 2:", add_invalid(inputs, iswrong2))
