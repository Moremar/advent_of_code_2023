#!/usr/bin/env python3
import re
import time
import numpy as np


def parse(input_path):
    with open(input_path, 'r') as f:
        hailstones = []
        for (i, line) in enumerate(f.readlines()):
            x, y, z, vx, vy ,vz = re.findall(r'(-?\d+)', line)
            hailstones.append(((int(x), int(y), int(z)), (int(vx), int(vy), int(vz))))
        return hailstones


def solve_p1(hailstones, min_zone, max_zone):
    total = 0
    for i in range(len(hailstones)):
        for j in range(i+1, len(hailstones)):
            (pi, vi), (pj, vj) = hailstones[i], hailstones[j]
            assert vi[0] != 0 and vj[0] != 0

            # represent both lines as y = ax + b
            a_i = vi[1] / vi[0]
            b_i = pi[1] - a_i * pi[0]
            a_j = vj[1] / vj[0]
            b_j = pj[1] - a_j * pj[0]

            if a_i == a_j:
                # parallel lines, no intersection
                assert b_i != b_j
                continue

            # find intersection point
            left_part = np.array([[1, -a_i], [1, -a_j]])
            right_part = np.array([b_i, b_j])
            y, x = np.linalg.solve(left_part, right_part)

            if not min_zone <= x <= max_zone or not min_zone <= y <= max_zone:
                # not inside the target zone
                continue
            elif (y > pi[1] and vi[1] < 0) or (y < pi[1] and vi[1] > 0):
                # the intersection is in the past for hailstone i
                continue
            elif (y > pj[1] and vj[1] < 0) or (y < pj[1] and vj[1] > 0):
                # the intersection is in the past for hailstone j
                continue
            else:
                total += 1
    return total


if __name__ == "__main__":
    start = time.time()
    hailstones = parse("data.txt")
    result = solve_p1(hailstones, 200000000000000, 400000000000000)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
