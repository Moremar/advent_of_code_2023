#!/usr/bin/env python3
import time
import re


def parse(input_path):
    res = []
    with open(input_path, 'r') as f:
        for line in f.readlines():
            game = []
            for block in line[line.index(':'):].split(';'):
                match = re.search(r'(\d+) red', block)
                red = int(match.groups()[0]) if match is not None else 0
                match = re.search(r'(\d+) green', block)
                green = int(match.groups()[0]) if match is not None else 0
                match = re.search(r'(\d+) blue', block)
                blue = int(match.groups()[0]) if match is not None else 0
                game.append((red, green, blue))
            res.append(game)
        return res


def solve(games):
    return sum([i+1 for (i, game) in enumerate(games)
                if all([cubes[0] <= 12 and cubes[1] <= 13 and cubes[2] <= 14 for cubes in game])])


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve(parsed)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
