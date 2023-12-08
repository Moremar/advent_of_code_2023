#!/usr/bin/env python3
import re
import time


def parse(input_path):
    with open(input_path, 'r') as f:
        return (list(map(int, re.findall(r'(\d+)', line))) for line in f.readlines())


def solve(times, records):
    result = 1
    for race_id in range(len(times)):
        wins = 0
        for i in range(1, times[race_id]):
            if i * (times[race_id] - i) > records[race_id]:
                wins += 1
        result *= wins
    return result


if __name__ == "__main__":
    start = time.time()
    times, records = parse("data.txt")
    result = solve(times, records)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
