#!/usr/bin/env python3
import time
from part1 import parse


def solve(cards):
    copies = {card_id : 1 for card_id in range(len(cards))}
    for (card_id, card) in enumerate(cards):
        points = sum([1 for my_nb in card[1] if my_nb in card[0]])
        for i in range(points):
            copies[card_id + 1 + i] += copies[card_id]
    return sum([copies[card_id] for card_id in copies])


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve(parsed)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
