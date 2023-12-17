#!/usr/bin/env python3
import time
from part1 import parse, find_lowest_heat_loss, RIGHT, DOWN


def solve(world):
    return find_lowest_heat_loss(world, [((0, 0), RIGHT, 0, 0),((0, 0), DOWN, 0, 0)], 10, 4)


if __name__ == "__main__":
    start = time.time()
    world = parse("data.txt")
    result = solve(world)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
