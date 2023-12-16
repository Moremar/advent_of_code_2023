#!/usr/bin/env python3
import time
from part1 import parse, count_energized_tiles, UP, DOWN, LEFT, RIGHT


def solve(world):
    max_i = max([i for i,j in world])
    max_j = max([j for i,j in world])
    initial_states = [((i, -1),      RIGHT) for i in range(max_i)] \
                   + [((i, max_j+1), LEFT)  for i in range(max_i)] \
                   + [((-1, j),      DOWN)  for j in range(max_j)] \
                   + [((max_i+1, j), UP)    for j in range(max_j)]
    return max([count_energized_tiles(world, state) for state in initial_states])


if __name__ == "__main__":
    start = time.time()
    world = parse("data.txt")
    result = solve(world)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
