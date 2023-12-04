#!/usr/bin/env python3
import time


def parse(input_path):
    cards = []
    with open(input_path, 'r') as f:
        for line in f.readlines():
            left, right = line.split(':')[1].split('|')
            cards.append((left.split(), right.split()))
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
