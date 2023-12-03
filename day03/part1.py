#!/usr/bin/env python3
import time

WORLD = {}


def parse(input_path):
    with open(input_path, 'r') as f:
        for (i, line) in enumerate(f.readlines()):
            for j, c in enumerate(line.strip()):
                WORLD[(i, j)] = c


def get_neighbors(point):
    i, j = point
    return [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]


def solve():
    max_i = max([i for (i, j) in WORLD])
    max_j = max([j for (i, j) in WORLD])
    total = 0
    number, valid = 0, False
    for i in range(max_i+1):
        for j in range(max_j+1):
            if WORLD[(i,j)].isdigit():
                # build the current number and keep track if it is valid so far
                number = 10 * number + int(WORLD[(i,j)])
                if not valid:
                    for neighbor in get_neighbors((i, j)):
                        if neighbor in WORLD and not WORLD[neighbor].isdigit() and not WORLD[neighbor] == '.':
                            valid = True
                            break
            elif number != 0:
                # a number was just completed, add it if it is valid
                if valid:
                    total += number
                number, valid = 0, False
    return total


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve()
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')











# def parse(input_path):
#     M = {}
#     with open(input_path, 'r') as f:
#         X = 0
#         for (i, line) in enumerate(f.readlines()):
#             Y = len(line.strip())
#             for j, c in enumerate(line.strip()):
#                 M[(i, j)] = c
#             X = X + 1
#         return M, X, Y
#
# def get_neighbors(coords):
#     x, y = coords
#     return [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]
#
# def solve(a):
#     M, X, Y = a
#     total = 0
#     digit = 0
#     valid_digit = False
#     for i in range(X):
#         for j in range(Y):
#             if M[(i,j)].isdigit():
#                 digit = 10 * digit + int(M[(i,j)])
#                 if not valid_digit:
#                     for neighbor in get_neighbors((i, j)):
#                         if neighbor in M and not M[neighbor].isdigit() and not M[neighbor] == '.':
#                             valid_digit = True
#                             break
#             elif digit != 0:
#                 if valid_digit:
#                     total += digit
#                 digit = 0
#                 valid_digit = False
#     return total
#
