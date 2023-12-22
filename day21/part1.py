#!/usr/bin/env python3
import time


def parse(input_path):
    with open(input_path, 'r') as f:
        world, s_pos = set(), None
        lines = f.read().split('\n')
        for i in range(len(lines)):
            for j in range(len(lines[0])):
                if lines[i][j] == 'S':
                    s_pos = (i, j)
                if lines[i][j] in 'S.':
                    world.add((i, j))
        return world, s_pos


def solve(world, s_pos):
    reachable_pos = {s_pos}
    for k in range(64):
        positions = set()
        for (i, j) in reachable_pos:
            for p in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if p in world:
                    positions.add(p)
        reachable_pos = positions
    return len(reachable_pos)


if __name__ == "__main__":
    start = time.time()
    world, s_pos = parse("data.txt")
    result = solve(world, s_pos)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
