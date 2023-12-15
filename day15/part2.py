#!/usr/bin/env python3
import re
import time
from part1 import get_hash


def parse(input_path):
    with open(input_path, 'r') as f:
        return [re.match(r'^(.+)([=\-])(.*)$', token).groups() for token in f.read().strip().split(',')]


def remove_lens(boxes, box_id, label):
    for i in range(len(boxes[box_id])):
        if boxes[box_id][i][0] == label:
            del boxes[box_id][i]
            return


def upsert_lens(boxes, box_id, label, strength):
    for i in range(len(boxes[box_id])):
        if boxes[box_id][i][0] == label:
            boxes[box_id][i] = (label, int(strength))
            return
    boxes[box_id].append((label, int(strength)))


def solve(tokens):
    boxes = { i: [] for i in range(256) }
    for (label, operator, strength) in tokens:
        if operator == '-':
            remove_lens(boxes, get_hash(label), label)
        else:
            upsert_lens(boxes, get_hash(label), label, strength)
    return sum([(1 + box_id) * (i + 1) * lens[1]
                for box_id in range(256)
                for (i, lens) in enumerate(boxes[box_id])])


if __name__ == "__main__":
    start = time.time()
    tokens = parse("data.txt")
    result = solve(tokens)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
