#!/usr/bin/env python3
import time


class PipeNode:
    def __init__(self, coord, shape, connected):
        self.coord = coord
        self.shape = shape
        self.connected = connected


def parse(input_path):
    with open(input_path, 'r') as f:
        world = {}
        lines = [l.strip() for l in f.readlines()]
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                world[(i, j)] = lines[i][j]
        return world


def get_s_pipe(p, world):
    possible = '-|J7LF'
    if (p[0], p[1]-1) in world and world[(p[0], p[1]-1)] in 'L-F':
        possible = [c for c in possible if c in 'J-7']
    if (p[0], p[1]+1) in world and world[(p[0], p[1]+1)] in 'J-7':
        possible = [c for c in possible if c in 'L-F']
    if (p[0]-1, p[1]) in world and world[(p[0]-1, p[1])] in '7|F':
        possible = [c for c in possible if c in 'J|L']
    if (p[0]+1, p[1]) in world and world[(p[0]+1, p[1])] in 'J|L':
        possible = [c for c in possible if c in '7|F']
    assert len(possible) == 1
    return possible[0]


def get_connected_coords(p, world):
    res = []
    if world[p] in 'J|L':
        res.append((p[0]-1, p[1]))
    if world[p] in '7|F':
        res.append((p[0]+1, p[1]))
    if world[p] in '7-J':
        res.append((p[0], p[1]-1))
    if world[p] in 'L-F':
        res.append((p[0], p[1]+1))
    return res


def init_pipe_nodes(world):
    pipe_nodes = {}
    start = None
    for p in world:
        if world[p] == 'S':
            start = p
            world[p] = get_s_pipe(p, world)
        connected = get_connected_coords(p, world)
        if len(connected):
            pipe_nodes[p] = PipeNode(p, world[p], connected)
    return start, pipe_nodes


def build_pipe(start, pipes):
    pipe = [pipes[start]]
    curr = start
    prev = None
    while True:
        connected = pipes[curr].connected
        prev, curr = curr, connected[0] if connected[0] != prev else connected[1]
        pipe.append(pipes[curr])
        if len(pipe) > 2 and start in pipes[curr].connected:
            return pipe


def solve(world):
    start, pipe_nodes = init_pipe_nodes(world)
    pipe = build_pipe(start, pipe_nodes)
    return (len(pipe) + 1) // 2


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve(parsed)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
