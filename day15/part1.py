#!/usr/bin/env python3
import time


def parse(input_path):
    with open(input_path, 'r') as f:
        return f.read().strip().split(',')


def get_hash(s):
    curr = 0
    for c in s:
        curr = (curr + ord(c)) * 17 % 256
    return curr


def solve(tokens):
    return sum([get_hash(token) for token in tokens])


if __name__ == "__main__":
    start = time.time()
    tokens = parse("data.txt")
    result = solve(tokens)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
