#!/usr/bin/env python3
import re
import time


def parse(input_path):
    with open(input_path, 'r') as f:
        lines = f.readlines()
        directions = [(0 if c == 'L' else 1) for c in lines[0].strip()]
        transitions = {}
        for line in lines[2:]:
            source, left, right = re.findall(r'\w+', line.strip())
            transitions[source] = (left, right)
        return directions, transitions


def solve(directions, transitions):
    curr, step = 'AAA', 0
    while True:
        curr = transitions[curr][directions[step % len(directions)]]
        step += 1
        if curr == 'ZZZ':
            return step


if __name__ == "__main__":
    start = time.time()
    directions, transitions = parse("data.txt")
    result = solve(directions, transitions)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
