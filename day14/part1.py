#!/usr/bin/env python3
import time


def parse(input_path):
    with open(input_path, 'r') as f:
        rocks, balls = set(), set()
        for (i, line) in enumerate([l.strip() for l in f.readlines()]):
            for (j, c) in enumerate(line):
                if c == 'O':
                    balls.add((i, j))
                elif c == '#':
                    rocks.add((i,j))
        return rocks, balls, i+1, j+1


def tilt_north(rocks, balls, len_i, len_j):
    next_balls = set()
    for i in range(len_i):
        for j in range(len_j):
            if (i, j) in balls:
                new_i = i
                while new_i > 0 and (new_i - 1, j) not in next_balls and (new_i - 1, j) not in rocks:
                    new_i = new_i - 1
                next_balls.add((new_i, j))
    return next_balls


def calculate_load(balls, len_i):
    return sum([len_i - i for (i, j) in balls])


def solve(rocks, balls, len_i, len_j):
    return calculate_load(tilt_north(rocks, balls, len_i, len_j), len_i)


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve(*parsed)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
