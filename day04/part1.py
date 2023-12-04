#!/usr/bin/env python3
import time
import re


def parse(input_path):
    cards = []
    with open(input_path, 'r') as f:
        for line in f.readlines():
            # the number of spaces between the integers varies, so we remove extra spaces
            left, right = re.sub(r' +', ' ', line).split(':')[1].split('|')
            win_nbs = [int(x) for x in left.strip().split(' ')]
            my_nbs = [int(x) for x in right.strip().split(' ')]
            cards.append((win_nbs, my_nbs))
        return cards


def solve(cards):
    total_score = 0
    for card in cards:
        card_score = 0
        for my_nb in card[1]:
            if my_nb in card[0]:
                card_score = card_score * 2 if card_score else 1
        total_score += card_score
    return total_score


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve(parsed)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
