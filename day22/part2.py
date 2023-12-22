#!/usr/bin/env python3
import time
from part1 import parse, get_stable_state


def count_falling_bricks(bricks, brick_id):
    to_check = {(bricks[carried_id].start.z, carried_id) for carried_id in bricks[brick_id].carry}
    falling = {brick_id}
    while len(to_check):
        # we store each brick to check along with its lowest z, to check them from the lowest to highest
        # this way we are sure that when we process a brick, all its carriers have been checked already
        (curr_z, curr_id) = min(to_check)
        to_check.remove((curr_z, curr_id))
        if all([carrier in falling for carrier in bricks[curr_id].carried_by]):
            falling.add(curr_id)
            for carried in bricks[curr_id].carry:
                if carried not in falling:
                    carried_z = bricks[carried].start.z
                    if (carried_z, carried) not in to_check:
                        to_check.add((carried_z, carried))
    return len(falling) - 1  # -1 for initial one


def solve(bricks):
    bricks = get_stable_state(bricks)
    return sum([count_falling_bricks(bricks, brick_id) for brick_id in bricks])


if __name__ == "__main__":
    start = time.time()
    bricks = parse("data.txt")
    result = solve(bricks)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
