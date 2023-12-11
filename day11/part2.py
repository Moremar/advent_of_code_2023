#!/usr/bin/env python3
import time
from part1 import parse, solve


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve(*parsed, factor=1000000)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
