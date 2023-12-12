#!/usr/bin/env python3
import time
from part1 import parse, solve


def get_unfolded_input(parsed):
    return [('?'.join([springs] * 5), contiguous * 5) for (springs, contiguous) in parsed]


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve(get_unfolded_input(parsed))
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
