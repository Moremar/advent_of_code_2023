#!/usr/bin/env python3
import time
from collections import deque

UP, DOWN, LEFT, RIGHT = (-1, 0),  (1, 0),  (0, -1),  (0, 1)


def parse(input_path):
    with open(input_path, 'r') as f:
        return {(i, j): int(c) for (i, line) in enumerate(f.read().split('\n')) for (j, c) in enumerate(line)}


def add_2d(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1])


def get_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def find_lowest_heat_loss(world, initial_state, max_consecutive, min_consecutive):
    target_position = (max([i for (i, j) in world]), max([j for (i, j) in world]))
    seen = {}
    lowest_heat_loss = None
    to_process = deque(initial_state)
    while len(to_process):
        position, prev_direction, steps, heat_loss = to_process.popleft()
        # keep processing this path as far as we can
        while True:
            valid_moves = []
            preferred_direction = None
            for direction in [UP, DOWN, LEFT, RIGHT]:
                # cant go back to where we come from
                if add_2d(direction, prev_direction) == (0, 0):
                    continue
                # cant change direction before the min steps
                if min_consecutive > 0 and direction != prev_direction and steps < min_consecutive:
                    continue
                # cant do more than the max steps in the same direction
                if prev_direction == direction and steps == max_consecutive:
                    continue
                # cant go outside the map
                next_position = add_2d(position, direction)
                if next_position not in world:
                    continue
                # discard if we already found a better path
                next_heat_loss = heat_loss + world[next_position]
                if lowest_heat_loss is not None and next_heat_loss > lowest_heat_loss:
                    continue
                # discard if already calculated
                next_steps = steps + 1 if direction == prev_direction else 1
                similar_keys = [(next_position, direction, k) for k in range(min_consecutive, next_steps+1)]
                if any([key in seen and seen[key] <= next_heat_loss for key in similar_keys]):
                    continue
                seen[(next_position, direction, next_steps)] = next_heat_loss
                # record the best score if we reached the target
                if next_position == target_position:
                    if lowest_heat_loss is None or lowest_heat_loss > next_heat_loss:
                        lowest_heat_loss = next_heat_loss
                    continue
                # among possible moves, keep track of the one physically closer to the target
                valid_moves.append((direction, next_position, next_steps, next_heat_loss))
                dist_to_target = get_distance(next_position, target_position)
                if preferred_direction is None or dist_to_target < preferred_direction[1]:
                    preferred_direction = (direction, dist_to_target)
            # this path we are following has no further branches to explore
            if len(valid_moves) == 0:
                break
            # follow the path physically closest to the target and keep track of the others for later processing
            # this way, we quickly get a first distance to the target allowing to discard longer paths
            for (direction, next_position, next_steps, next_heat_loss) in valid_moves:
                if direction == preferred_direction[0]:
                    position, prev_direction, steps, heat_loss = next_position, direction, next_steps, next_heat_loss
                else:
                    to_process.append((next_position, direction, next_steps, next_heat_loss))
    return lowest_heat_loss


def solve(world):
    return find_lowest_heat_loss(world, [((0, 0), RIGHT, 0, 0)], 3, 0)


if __name__ == "__main__":
    start = time.time()
    world = parse("data.txt")
    result = solve(world)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
