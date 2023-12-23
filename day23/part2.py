#!/usr/bin/env python3
import time
from part1 import parse, get_adj, stringify


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.adj = {}


def build_graph(world):
    graph = {}
    # build nodes
    for p in world:
        graph[p] = Node(p[0], p[1])
        for adj_p in get_adj(p):
            if adj_p in world:
                graph[p].adj[adj_p] = 1
    # simplify nodes
    entries = [p for p in graph]
    for p in entries:
        if len(graph[p].adj) == 2:
            p1, p2 = graph[p].adj.keys()
            dist_p1_p2 = graph[p].adj[p1] + graph[p].adj[p2]
            assert p2 not in graph[p1].adj and p1 not in graph[p2].adj  # never 2 ways to go from p1 to p2
            graph[p1].adj[p2] = dist_p1_p2
            graph[p2].adj[p1] = dist_p1_p2
            del graph[p1].adj[p]
            del graph[p2].adj[p]
            del graph[p]
    return graph


def solve(world, initial_p, target):
    graph = build_graph(world)
    to_check = [(0, initial_p, {initial_p})]
    seen = {(initial_p, stringify([initial_p])): 0}
    best_score = 0
    while len(to_check):
        score, curr_p, visited = max(to_check)
        to_check.remove((score, curr_p, visited))
        for next_p in graph[curr_p].adj:
            if next_p in visited:
                continue
            next_score = score + graph[curr_p].adj[next_p]
            next_visited = set(visited)
            next_visited.add(next_p)
            hash = stringify(next_visited)
            if (next_p, hash) in seen and seen[(next_p, hash)] >= next_score:
                continue
            seen[(next_p, hash)] = next_score
            if next_p == target and best_score < next_score:
                best_score = next_score
            else:
                to_check.append((next_score, next_p, next_visited))
    return best_score


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve(*parsed)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
