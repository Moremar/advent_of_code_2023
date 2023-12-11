#!/usr/bin/env python3
import time


def parse(input_path):
    with open(input_path, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        galaxies = [(i, j) for i in range(len(lines)) for j in range(len(lines[0])) if lines[i][j] == '#']
        return galaxies, len(lines), len(lines[0])


def solve(galaxies, max_i, max_j, factor):
    expansion_i = [i for i in range(max_i) if all([p[0] != i for p in galaxies])]
    expansion_j = [j for j in range(max_j) if all([p[1] != j for p in galaxies])]
    expanded = []
    for galaxy in galaxies:
        shift_i = len([1 for x in expansion_i if x < galaxy[0]]) * (factor - 1)
        shift_j = len([1 for x in expansion_j if x < galaxy[1]]) * (factor - 1)
        expanded.append((galaxy[0] + shift_i, galaxy[1] + shift_j))
    return sum([abs(expanded[i][0] - expanded[j][0]) + abs(expanded[i][1] - expanded[j][1])
                for i in range(len(expanded)-1)
                for j in range(i, len(expanded))])


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve(*parsed, factor=2)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
