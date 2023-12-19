#!/usr/bin/env python3
import time
from collections import deque
from functools import reduce
from part1 import parse


def solve(workflows):
    score = 0
    to_process = deque([({ category: (1, 4000) for category in 'xmas' }, 'in')])
    while len(to_process):
        part, workflow_id = to_process.popleft()
        workflow_id, split_parts = workflows[workflow_id].process_interval(part)
        if workflow_id == 'R':
            continue
        if workflow_id == 'A':
            score += reduce(lambda x, y: x * y, [part[category][1] - part[category][0] + 1 for category in 'xmas'])
            continue
        for split_part in split_parts:
            to_process.append((split_part, workflow_id))
    return score


if __name__ == "__main__":
    start = time.time()
    workflows, _ = parse("data.txt")
    result = solve(workflows)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
