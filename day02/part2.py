#!/usr/bin/env python3
import time
from part1 import parse


def solve(parsed):
    res = 0
    for (i, games) in enumerate(parsed):
        min_red = min_green = min_blue = 0
        for game in games:
            min_red = max(min_red, game[0])
            min_green = max(min_green, game[1])
            min_blue = max(min_blue, game[2])
        res += min_green * min_red * min_blue
    return res


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve(parsed)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
