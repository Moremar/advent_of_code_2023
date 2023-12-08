#!/usr/bin/env python3
import time
from part1 import parse
import math


def solve(directions, transitions):
    starts = [k for k in transitions if k[-1] == 'A']
    metrics = []
    for k in range(len(starts)):
        curr = starts[k]
        seen = {(curr, 0)}
        seen_step = {(curr, 0): 0}
        cycle_found = False
        cycle_size = -1
        step = 0
        while True:
            curr = transitions[curr][directions[step % len(directions)]]
            step += 1

            if not cycle_found:
                # look for a cycle
                if (curr, step % len(directions)) in seen:
                    cycle_found = True
                    cycle_start = seen_step[(curr, step % len(directions))]
                    cycle_size = step - cycle_start
                else:
                    # record the current state (node + position in the directions)
                    seen.add((curr, step % len(directions)))
                    seen_step[(curr, step % len(directions))] = step

            if cycle_found and curr[-1] == 'Z':
                # we record 2 metrics : the number of steps needed to reach the first Z state, and the cycle size
                metrics.append((step - cycle_size, cycle_size))
                break

    # In the metrics array, all our integer pairs have 2 equal numbers.
    # This means that all cycle sizes are equal to the number of steps needed to reach the first Z state
    # That is very convenient, it means that for all ghosts to reach a Z state simultaneously, we just need
    # to find a number of steps that is a multiple of the cycle size for each starting state
    # The smallest of these numbers is the LCM (Lowest Common Multiple) of the cycle sizes
    return math.lcm(*[metric[0] for metric in metrics])


if __name__ == "__main__":
    start = time.time()
    directions, transitions = parse("data.txt")
    result = solve(directions, transitions)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')