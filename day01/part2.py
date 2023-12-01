#!/usr/bin/env python3
import time

DIGITS = {'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine': 9}


def parse(input_path):
    res = []
    with open(input_path, 'r') as f:
        for line in f.readlines():
            first = None
            for i in range(len(line)):
                # find first digit in the string
                if line[i].isdigit():
                    first = int(line[i])
                    break
                for digit_str in DIGITS:
                    if line[i:].startswith(digit_str):
                        first = DIGITS[digit_str]
                        break
                if first is not None:
                    break
            # find last digit in the string
            last = None
            for i in range(len(line)):
                if line[-1-i].isdigit():
                    last = int(line[-1-i])
                    break
                for digit in DIGITS:
                    if line[-1-i:].startswith(digit):
                        last = DIGITS[digit]
                        break
                if last is not None:
                    break
            res.append(first * 10 + last)
        return res


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = sum(parsed)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
