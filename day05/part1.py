#!/usr/bin/env python3
import time


def parse(input_path):
    with open(input_path, 'r') as f:
        lines = f.readlines()
        seeds = [int(x) for x in lines[0].split(": ")[1].split()]
        transitions = []
        for line in lines[2:]:
            if 'map' in line:
                transitions.append([])
            elif len(line.strip()):
                transitions[-1].append([int(x) for x in line.split()])
        return seeds, transitions


def solve(seeds, transitions):
    numbers = seeds
    next_numbers = []
    for transition in transitions:
        for number in numbers:
            found_rule = False
            for (start_dest, start_source, range_len) in transition:
                if start_source <= number < start_source + range_len:
                    next_numbers.append(start_dest + (number - start_source))
                    found_rule = True
                    break
            if not found_rule:
                next_numbers.append(number)
        numbers = next_numbers
        next_numbers = []
    return min(numbers)


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve(*parsed)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
