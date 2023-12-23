#!/usr/bin/env python3
import time
from collections import deque


def parse(input_path):
    with open(input_path, 'r') as f:
        world = {}
        lines = [l.strip() for l in f.readlines()]
        for (i, line) in enumerate(lines):
            for (j, c) in enumerate(line):
                if c in '.><v^':
                    world[(i, j)] = c
                    if i == 0:
                        initial_p = (i, j)
                    if i == len(lines)-1:
                        target = (i, j)
        return world, initial_p, target


def add_p(p1, p2):
    return p1[0] + p2[0], p1[1] + p2[1]


def get_adj(p):
    return [add_p(p, direction) for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]]


def stringify(set_p):
    return '_'.join([f'{p[0]}-{p[1]}' for p in set_p])


def solve(world, initial_p, target_p):
    to_check = deque([(initial_p, {initial_p})])
    seen = {(initial_p, stringify([initial_p]))}
    best_score = 0
    while len(to_check):
        curr_p, visited = to_check.popleft()
        for next_p in get_adj(curr_p):
            if next_p in world and next_p not in visited:
                next_visited = set(visited)
                next_visited.add(next_p)
                hash = stringify(next_visited)
                if (next_p, hash) in seen:
                    continue
                seen.add((next_p, hash))
                forbidden_slide = False
                while world[next_p] in '<>v^':
                    if world[next_p] == '<':
                        next_p = add_p(next_p, (0, -1))
                    elif world[next_p] == '>':
                        next_p = add_p(next_p, (0, 1))
                    elif world[next_p] == 'v':
                        next_p = add_p(next_p, (1, 0))
                    elif world[next_p] == '^':
                        next_p = add_p(next_p, (-1, 0))
                    if next_p in next_visited:
                        forbidden_slide = True   # slided on a cell already seen
                        break
                    next_visited.add(next_p)
                if forbidden_slide:
                    continue
                if next_p == target_p and best_score < len(next_visited):
                    best_score = len(next_visited)
                else:
                    to_check.append((next_p, next_visited))
    return best_score - 1  # -1 because the start node does not count


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve(*parsed)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
