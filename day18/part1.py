#!/usr/bin/env python3
import re
import time

UP, DOWN, LEFT, RIGHT = (-1, 0),  (1, 0),  (0, -1),  (0, 1)


def parse(input_path):
    with open(input_path, 'r') as f:
        instructions = []
        directions_map = { 'U': UP, 'D': DOWN, 'R': RIGHT, 'L': LEFT }
        lines = [l.strip() for l in f.readlines()]
        for line in lines :
            direction, steps = re.match(r'^(.*) (.*) ', line).groups()
            instructions.append((directions_map[direction], int(steps)))
        return instructions


def merge_intervals(intervals):
    intervals = sorted(intervals)
    merged = []
    curr = intervals[0]
    for interval in intervals[1:]:
        if interval[0] > curr[1]:
            merged.append(curr)
            curr = interval
        else:
            curr = (curr[0], max(curr[1], interval[1]))
    merged.append(curr)
    return merged


def count_cubic_meters(world):
    cubic_meters = 0
    curr_intervals = []
    prev_i = None
    for i in sorted({p[0] for p in world}):
        # add cubic meters for skipped lines
        for curr_interval in curr_intervals:
            cubic_meters += (i - prev_i - 1) * (curr_interval[1] - curr_interval[0] + 1)
        prev_i = i
        # find the intervals on the current row
        edges = sorted([p[1] for p in world if p[0] == i])
        row_intervals = [(edges[2 * k], edges[2 * k + 1]) for k in range(len(edges) // 2)]
        # count the cubic meters on the current row
        for (a, b) in merge_intervals(row_intervals + curr_intervals):
            cubic_meters += b - a + 1
        # update the ongoing intervals
        for (j1, j2) in row_intervals:
            replaced = False
            for (a, b) in curr_intervals:
                if a <= j1 <= b and a <= j2 <= b:
                    curr_intervals.remove((a, b))
                    if a != j1:
                        curr_intervals.append((a, j1))
                    if b != j2:
                        curr_intervals.append((j2, b))
                    replaced = True
                    break
            if not replaced:
                curr_intervals.append((j1, j2))
                curr_intervals = merge_intervals(curr_intervals)
    return cubic_meters


def solve(parsed):
    world, pos = set(), (0, 0)
    for direction, steps in parsed:
        world.add(pos)
        pos = pos[0] + steps * direction[0], pos[1] + steps * direction[1]
    return count_cubic_meters(world)


if __name__ == "__main__":
    start = time.time()
    instructions = parse("data.txt")
    result = solve(instructions)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
