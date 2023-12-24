#!/usr/bin/env python3
import time
from sympy import symbols, Eq
from sympy.solvers import solve
from part1 import parse

# We have 6 unknown values that we are looking for :
#   - the rock starting position (x_rock, y_rock, z_rock)
#   - the rock velocity (vx_rock, vy_rock, vz_rock)
# We know that the rock hits each hailstone i at a given millisecond ti, so :
#   x_rock + ti * vx_rock = x_i + ti * vx_i
#   y_rock + ti * vy_rock = y_i + ti * vy_i
#   z_rock + ti * vz_rock = z_i + ti * vz_i
# So each hailstone gives us 3 equation and adds one unknown value (the ti when the rock hits this hailstone)
# By considering the first 3 hailstones, we get a system of 9 equations with 9 unknown values.
# This can be solved by the sympy solver.


def solve_p2(parsed):
    # create the 9 unknown values
    x_rock, y_rock, z_rock = symbols('x_rock y_rock z_rock')
    vx_rock, vy_rock, vz_rock = symbols('vx_rock vy_rock vz_rock')
    t0, t1, t2 = symbols('t0 t1 t2')
    # create the 9 equations
    (p0, v0), (p1, v1), (p2, v2) = parsed[0], parsed[1], parsed[2]
    eq_0_x = Eq(x_rock + t0 * vx_rock, p0[0] + t0 * v0[0])
    eq_0_y = Eq(y_rock + t0 * vy_rock, p0[1] + t0 * v0[1])
    eq_0_z = Eq(z_rock + t0 * vz_rock, p0[2] + t0 * v0[2])
    eq_1_x = Eq(x_rock + t1 * vx_rock, p1[0] + t1 * v1[0])
    eq_1_y = Eq(y_rock + t1 * vy_rock, p1[1] + t1 * v1[1])
    eq_1_z = Eq(z_rock + t1 * vz_rock, p1[2] + t1 * v1[2])
    eq_2_x = Eq(x_rock + t2 * vx_rock, p2[0] + t2 * v2[0])
    eq_2_y = Eq(y_rock + t2 * vy_rock, p2[1] + t2 * v2[1])
    eq_2_z = Eq(z_rock + t2 * vz_rock, p2[2] + t2 * v2[2])
    # solve the system
    solved = solve((eq_0_x, eq_0_y, eq_0_z, eq_1_x, eq_1_y, eq_1_z, eq_2_x, eq_2_y, eq_2_z),
                   (x_rock, y_rock, z_rock, vx_rock, vy_rock, vz_rock, t0, t1, t2))
    # sum the initial coordinates of the rock
    return solved[0][0] + solved[0][1] + solved[0][2]


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve_p2(parsed)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
