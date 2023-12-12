#!/usr/bin/env python3
import time

# cache the results of the get_count function to avoid calling it multiple identical computations
CACHE = {}


def parse(input_path):
    with open(input_path, 'r') as f:
        result = []
        for line in f.readlines():
            springs, contiguous = line.strip().split(' ')
            result.append((springs, list(map(int, contiguous.split(',')))))
        return result


def get_count(spring_idx, curr_spring, contiguous_idx, curr_contiguous, in_sequence, springs, contiguous):
    # check if the result is already in cache
    cache_key = (spring_idx, curr_spring, contiguous_idx, curr_contiguous, in_sequence)
    if cache_key in CACHE:
        return CACHE[cache_key]

    # end condition, when the springs row has been entirely processed
    if spring_idx == len(springs):
        all_verified = contiguous_idx == len(contiguous) \
                       or (in_sequence and contiguous_idx == len(contiguous) - 1 and curr_contiguous == 0)
        return 1 if all_verified else 0

    if curr_spring is None:
        curr_spring = springs[spring_idx]

    if curr_contiguous is None:
        curr_contiguous = 0 if contiguous_idx == len(contiguous) else contiguous[contiguous_idx]

    # when a spring state is unknown, try both possible states and cache the result
    if curr_spring == '?':
        res = get_count(spring_idx, '.', contiguous_idx, curr_contiguous, in_sequence, springs, contiguous) \
            + get_count(spring_idx, '#', contiguous_idx, curr_contiguous, in_sequence, springs, contiguous)
        CACHE[cache_key] = res
        return res

    if in_sequence:
        if curr_spring == '.':
            if curr_contiguous != 0:
                return 0
            else:
                # end of the current damaged springs sequence
                return get_count(spring_idx + 1, None, contiguous_idx + 1, None, False, springs, contiguous)
        else:
            if curr_contiguous != 0:
                return get_count(spring_idx + 1, None, contiguous_idx, curr_contiguous - 1, True, springs, contiguous)
            else:
                return 0
    else:
        if curr_spring == '.':
            return get_count(spring_idx + 1, None, contiguous_idx, None, False, springs, contiguous)
        elif contiguous_idx == len(contiguous):
            return 0
        else:
            # start a new damaged springs sequence
            return get_count(spring_idx + 1, None, contiguous_idx, contiguous[contiguous_idx] - 1, True, springs, contiguous)


def get_arrangement_count(springs, contiguous):
    CACHE.clear()
    return get_count(0, None, 0, None, False, springs, contiguous)


def solve(parsed):
    return sum([get_arrangement_count(springs, contiguous) for (springs, contiguous) in parsed])


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve(parsed)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
