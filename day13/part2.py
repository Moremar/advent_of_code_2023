#!/usr/bin/env python3
import time
from part1 import parse, get_reflection_line


def flip(block, coord):
    block[coord] = '.' if block[coord] == '#' else '#'


def get_secondary_reflection_line(block):
    reflection_line = get_reflection_line(block)
    previous = None
    for coord in block:
        if previous is not None:
            flip(block, previous)
        flip(block, coord)
        previous = coord
        secondary_line = get_reflection_line(block, forbidden=reflection_line)
        if secondary_line != -1:
            return secondary_line


def solve(blocks):
    return sum([get_secondary_reflection_line(blocks[k]) for k in blocks])


if __name__ == "__main__":
    start = time.time()
    blocks = parse("data.txt")
    result = solve(blocks)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
