#!/usr/bin/env python3
import re
import time


def parse(input_path):
    with open(input_path, 'r') as f:
        return [list(map(int, re.findall(r'-*\d+', line.strip()))) for line in f.readlines()]


def compute_sequences(numbers):
    sequences = [numbers]
    while any([n != 0 for n in sequences[-1]]):
        sequences.append([sequences[-1][i+1]-sequences[-1][i] for i in range(len(sequences[-1])-1)])
    return sequences


def extrapolate(numbers):
    sequences = compute_sequences(numbers)
    sequences[-1].append(0)
    for i in range(len(sequences)-1):
        sequences[-1-i-1].append(sequences[-1-i-1][-1] + sequences[-1-i][-1])
    return sequences[0][-1]


def solve(parsed):
    return sum([extrapolate(numbers) for numbers in parsed])


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve(parsed)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
