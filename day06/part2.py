#!/usr/bin/env python3
import time
from part1 import parse, solve


if __name__ == "__main__":
    start = time.time()
    times, records = parse("data.txt")
    result = solve([int(''.join(map(str, times)))], [int(''.join(map(str, records)))])
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
