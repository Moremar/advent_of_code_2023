#!/usr/bin/env python3
import time
from collections import deque
from part1 import parse, build_pipe, init_pipe_nodes


def get_groups(pipe_node):
    x, y = pipe_node.coord
    if pipe_node.shape == '-':
        return [(x-1, y-1), (x-1, y), (x-1, y+1)], [(x+1, y-1), (x+1, y), (x+1, y+1)]
    if pipe_node.shape == '|':
        return [(x-1, y-1), (x, y-1), (x+1, y-1)], [(x-1, y+1), (x, y+1), (x+1, y+1)]
    if pipe_node.shape == 'J':
        return [(x-1, y-1)], [(x-1, y+1), (x, y+1), (x+1, y+1), (x+1, y), (x+1, y-1)]
    if pipe_node.shape == 'L':
        return [(x-1, y+1)], [(x-1, y-1), (x, y-1), (x+1, y-1), (x+1, y), (x+1, y+1)]
    if pipe_node.shape == 'F':
        return [(x+1, y+1)], [(x+1, y-1), (x, y-1), (x-1, y-1), (x-1, y), (x-1, y+1)]
    if pipe_node.shape == '7':
        return [(x+1, y-1)], [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]


def mark_groups(groupA, groupB, valA, zones, step):
    for p in groupA:
        zones[p] = (valA, step)
    for p in groupB:
        zones[p] = (1 - valA, step)


def assign_zone(p, pipe_points, world, zones):
    group = {p}
    zone_id = None
    to_process = deque({ p })
    seen = {p}
    while len(to_process):
        x, y = to_process.popleft()
        for neighbor in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if neighbor in world and neighbor not in seen and neighbor not in pipe_points:
                group.add(neighbor)
                to_process.append(neighbor)
                seen.add(neighbor)
                if neighbor in zones:
                    zone_id = zones[neighbor][0]
    for x in group:
        zones[x] = zone_id, len(pipe_points)


def solve(world):
    start, pipes = init_pipe_nodes(world)
    pipe = build_pipe(start, pipes)

    # split the world in zones 0 and 1 (we do not know yet which is inside and which is outside)
    # we record the zone ID (0 or 1) and the step where it was recorded
    # this is required because the points on the pipe can be marked in a zone at some point and change at a later stage
    # therefore when inferring the zone of a group of points, we only use the zone that were marked on the previous step
    zones = {}

    # separate the neighbors of the first pipe node between the 2 zones (inside and outside)
    group0, group1 = get_groups(pipe[0])
    mark_groups(group0, group1, 0, zones, 0)

    # for each pipe node, mark the zone of each neighbor point
    for i in range(1, len(pipe)):
        groupA, groupB = get_groups(pipe[i])  # we do not know which of group A and B is 0 and which is 1
        grouped = False
        for p in groupA:
            if p in zones and zones[p][1] == i-1:
                mark_groups(groupA, groupB, zones[p][0], zones, i)
                grouped = True
                break
        if not grouped:
            for p in groupB:
                if p in zones and zones[p][1] == i-1:
                    mark_groups(groupA, groupB, 1 - zones[p][0], zones, i)
                    grouped = True
                    break
        assert grouped

    # points that are not directly adjacent to a node of the pipe have no zone assigned
    # we mark their zone by doing a BFS limited by the world size and the nodes of the pipe
    pipe_points = [p.coord for p in pipe]
    for p in world:
        if p not in pipe_points and p not in zones:
            assign_zone(p, pipe_points, world, zones)

    # (0, 0) is outside the pipe, so the inside zone is the other zone
    target_zone_id = 1 - zones[(0, 0)][0]
    return len([x for x in world if x not in pipe_points and zones[x][0] == target_zone_id])


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve(parsed)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
