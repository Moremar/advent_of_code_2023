#!/usr/bin/env python3
import re
import time
from part1 import solve, UP, DOWN, LEFT, RIGHT


def parse(input_path):
    with open(input_path, 'r') as f:
        instructions = []
        directions_map = { '3': UP, '1': DOWN, '0': RIGHT, '2': LEFT }
        lines = [l.strip() for l in f.readlines()]
        for line in lines :
            color = re.match(r'^.* \(#(.*)\)', line).groups()[0]
            dist = int('0x' + color[:-1], 16)
            direction = directions_map[color[-1]]
            instructions.append((direction, dist))
        return instructions


if __name__ == "__main__":
    start = time.time()
    instructions = parse("data.txt")
    result = solve(instructions)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
