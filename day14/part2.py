#!/usr/bin/env python3
import time
from part1 import parse, calculate_load, tilt_north


def tilt_south(rocks, balls, len_i, len_j):
    next_balls = set()
    for i in range(len_i-1, -1, -1):
        for j in range(len_j):
            if (i, j) in balls:
                new_i = i
                while new_i < len_i - 1 and (new_i + 1, j) not in next_balls and (new_i + 1, j) not in rocks:
                    new_i = new_i + 1
                next_balls.add((new_i, j))
    return next_balls


def tilt_west(rocks, balls, len_i, len_j):
    next_balls = set()
    for j in range(len_j):
        for i in range(len_i):
            if (i, j) in balls:
                new_j = j
                while new_j > 0 and (i, new_j - 1) not in next_balls and (i, new_j - 1) not in rocks:
                    new_j = new_j - 1
                next_balls.add((i, new_j))
    return next_balls


def tilt_east(rocks, balls, len_i, len_j):
    next_balls = set()
    for j in range(len_j-1, -1, -1):
        for i in range(len_i):
            if (i, j) in balls:
                new_j = j
                while new_j < len_j - 1 and (i,new_j + 1) not in next_balls and (i, new_j + 1) not in rocks:
                    new_j = new_j + 1
                next_balls.add((i, new_j))
    return next_balls


def cycle(rocks, balls, len_i, len_j):
    balls = tilt_north(rocks, balls, len_i, len_j)
    balls = tilt_west(rocks, balls, len_i, len_j)
    balls = tilt_south(rocks, balls, len_i, len_j)
    return tilt_east(rocks, balls, len_i, len_j)


def hash_balls(balls):
    return '_'.join([str(i) + '-' + str(j) for (i, j) in balls])


def solve(rocks, balls, len_i, len_j):
    seen = {hash_balls(balls): 0}
    cycle_id = 0
    while True:
        cycle_id += 1
        balls = cycle(rocks, balls, len_i, len_j)
        balls_hash = hash_balls(balls)
        if balls_hash not in seen:
            seen[balls_hash] = cycle_id
        else:
            loop_size = cycle_id - seen[balls_hash]
            while cycle_id % loop_size != 1000000000 % loop_size:
                balls = cycle(rocks, balls, len_i, len_j)
                cycle_id += 1
            return calculate_load(balls, len_i)


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve(*parsed)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
