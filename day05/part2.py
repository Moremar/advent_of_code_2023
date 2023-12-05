#!/usr/bin/env python3
import time
from part1 import parse


def solve(seeds, transitions):
    # seeds are now pairs of (seed_start, seed_length)
    numbers = [(seeds[i*2], seeds[i*2+1]) for i in range(len(seeds)//2)]
    next_numbers = []
    for transition in transitions:
        curr_range_idx = 0
        while curr_range_idx < len(numbers):
            (nb_start, nb_len) = numbers[curr_range_idx]
            found_rule = False
            for start_dest, start_source, range_len in transition:
                # check if the start of the seed range is in the interval of a rule
                if start_source <= nb_start < start_source + range_len:
                    if nb_start + nb_len <= start_source + range_len:
                        # easy case, the full seed range is inside the same rule
                        next_numbers.append((start_dest + (nb_start - start_source), nb_len))
                    else:
                        # only part of the seed range is inside the rule, so we split the seed range into 2 parts
                        # the first part can be transitioned here, and we add the second part to be evaluated later
                        rule_max_len = start_source + range_len - nb_start
                        next_numbers.append((start_dest + (nb_start - start_source), rule_max_len))
                        numbers.append((nb_start + rule_max_len, nb_len - rule_max_len))
                    found_rule = True
                    break
            if not found_rule:
                # the seed start is not in any rule interval, but there may be a rule starting in the seed range
                # find the smallest rule start in the seed interval (if any)
                min_rule_start = None
                for (_, start_source, _) in transition:
                    if nb_start < start_source < nb_start + nb_len and (min_rule_start is None or start_source < min_rule_start):
                        min_rule_start = start_source
                if min_rule_start is None:
                    # easy case, the entire seed interval does not overlap with any rule interval
                    next_numbers.append((nb_start, nb_len))
                else:
                    # only the first part of the seed interval does not overlap with any rule, so we transition it now,
                    # and the second part of the interval will be evaluated later
                    next_numbers.append((nb_start, min_rule_start - nb_start))
                    numbers.append((min_rule_start, nb_start + nb_len - min_rule_start))

            curr_range_idx += 1
        numbers = next_numbers
        next_numbers = []
    return min([nb_start for (nb_start, nb_len) in numbers])


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve(*parsed)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
