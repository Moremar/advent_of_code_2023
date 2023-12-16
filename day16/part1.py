#!/usr/bin/env python3
import time
from collections import deque

UP, DOWN, LEFT, RIGHT = (-1, 0),  (1, 0),  (0, -1),  (0, 1)


def parse(input_path):
    with open(input_path, 'r') as f:
        return {(i, j): c for (i, line) in enumerate(f.read().split('\n')) for (j, c) in enumerate(line)}


def count_energized_tiles(world, initial_state):
    beams = deque([initial_state])
    energized = set()
    seen = set()
    while len(beams):
        # process a beam until it gets out of the map or reaches a previously processed state
        position, direction = beams.popleft()
        while True:
            position = (position[0] + direction[0], position[1] + direction[1])
            if position not in world or (position, direction) in seen:
                break
            energized.add(position)
            seen.add((position, direction))
            if world[position] == '/':
                if direction in [UP, RIGHT]:
                    direction = UP if direction == RIGHT else RIGHT
                else:
                    direction = DOWN if direction == LEFT else LEFT
            elif world[position] == '\\':
                if direction in [UP, LEFT]:
                    direction = UP if direction == LEFT else LEFT
                else:
                    direction = DOWN if direction == RIGHT else RIGHT
            elif world[position] == '-' and direction in [UP, DOWN]:
                beams.append((position, RIGHT))
                direction = LEFT
            elif world[position] == '|' and direction in [LEFT, RIGHT]:
                beams.append((position, DOWN))
                direction = UP
    return len(energized)


def solve(world):
    return count_energized_tiles(world, ((0, -1), RIGHT))


if __name__ == "__main__":
    start = time.time()
    world = parse("data.txt")
    result = solve(world)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
