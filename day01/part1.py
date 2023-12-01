#!/usr/bin/env python3
import time


def parse(input_path):
    res = []
    with open(input_path, 'r') as f:
        for line in f.readlines():
            # find first digit in the string
            for i in range(len(line)):
                if line[i].isdigit():
                    first = int(line[i])
                    break
            # find last digit in the string
            for i in range(len(line)):
                if line[-1-i].isdigit():
                    last = int(line[-1-i])
                    break
            res.append(first * 10 + last)
        return res


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = sum(parsed)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
