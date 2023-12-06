#!/usr/bin/env python3
import re


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
    times, records = parse("data.txt")
    print('Part 1 :', solve(times, records))
