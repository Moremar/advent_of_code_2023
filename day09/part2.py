#!/usr/bin/env python3
import time
from part1 import parse, compute_sequences


def extrapolate(numbers):
    sequences = compute_sequences(numbers)
    sequences[-1] = [0] + sequences[-1]
    for i in range(len(sequences)-1):
        sequences[-1-i-1] = [sequences[-1-i-1][0] - sequences[-1-i][0]] + sequences[-1-i-1]
    return sequences[0][0]


def solve(parsed):
    return sum([extrapolate(numbers) for numbers in parsed])


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve(parsed)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
