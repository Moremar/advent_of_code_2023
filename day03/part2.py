#!/usr/bin/env python3
import time
from part1 import parse, get_neighbors, WORLD


def get_number_start(point):
    i, j = point
    while (i, j-1) in WORLD and WORLD[(i, j-1)].isdigit():
        j = j-1
    return (i, j)


def get_number(point):
    i, j = point
    number = 0
    while (i, j) in WORLD and WORLD[(i, j)].isdigit():
        number = 10 * number + int(WORLD[(i, j)])
        j = j + 1
    return number


def solve():
    max_i = max([i for (i, j) in WORLD])
    max_j = max([j for (i, j) in WORLD])
    total = 0
    for i in range(max_i+1):
        for j in range(max_j+1):
            if WORLD[(i,j)] == '*':
                number_starts = { get_number_start(neighbor)
                                  for neighbor in get_neighbors((i, j))
                                  if neighbor in WORLD and WORLD[neighbor].isdigit() }
                if len(number_starts) == 2:
                    number_starts = list(number_starts)
                    total += get_number(number_starts[0]) * get_number(number_starts[1])
    return total


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve()
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
