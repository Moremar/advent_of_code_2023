#!/usr/bin/env python3
import time


def parse(input_path):
    with open(input_path, 'r') as f:
        world = {}
        for (k, block) in enumerate(f.read().split('\n\n')):
            world[k] = { (i, j) : line[j] for (i, line) in enumerate(block.split('\n')) for j in range(len(line)) }
        return world


def get_reflection_line(block, forbidden=-1):
    max_i, max_j = max([i for (i,j) in block]), max([j for (i, j) in block])
    # look for a vertical symmetry
    for j in range(0, max_j):
        is_symmetric = True
        for i in range(max_i+1):
            for dj in range(min(j+1, max_j-j)):
                if block[(i, j-dj)] != block[(i, j+1+dj)]:
                    is_symmetric = False
                    break
            if not is_symmetric:
                break
        if is_symmetric and forbidden != j + 1:
            return j + 1
    # look for a horizontal symmetry
    for i in range(0, max_i):
        is_symmetric = True
        for j in range(max_j+1):
            for di in range(min(i+1, max_i-i)):
                if block[(i-di, j)] != block[(i+1+di, j)]:
                    is_symmetric = False
                    break
            if not is_symmetric:
                break
        if is_symmetric and forbidden != 100 * (i + 1):
            return 100 * (i + 1)
    return -1


def solve(blocks):
    return sum([get_reflection_line(blocks[k]) for k in blocks])


if __name__ == "__main__":
    start = time.time()
    blocks = parse("data.txt")
    result = solve(blocks)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
