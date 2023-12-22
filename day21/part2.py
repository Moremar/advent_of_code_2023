import time
from numpy.polynomial.polynomial import polyfit
from part1 import parse

# We notice that the S is in the middle of a 131 x 131 grid, and there is no # in its row and column.
# This means that in exactly 65 steps, we can reach the end of the pattern in all 4 directions.
# Then every 131 steps further, we fill another pattern in each direction.
# Since it propagates in 2D, the number of plots increases in X^2.
# We try to find the function F such as F(x) = number of plots at step (x * 131 + 65)
# We want to express it as F(x) = ax^2 + bx + c
# For that, we calculate its value for x = 0, 1 and 2, and use the numpy polynomial solver to find the coefficients.
# We notice that the target step is 26501365 = 65 + 202300 * 131, so the result is F(202300)


def get_new_plots(world, to_check, prev_plots):
    new_plots = set()
    for (i, j) in to_check:
        for (px, py) in [(i+1,j), (i, j+1), (i-1,j), (i, j-1)]:
            if (px % 131, py % 131) in world and (px, py) not in prev_plots:
                new_plots.add((px, py))
    return new_plots


def find_quadratic_function(world, start):
    curr, prev = {start}, set()
    count_even, count_odd = 1, 0
    F = []
    for k in range(1, 65 + 2 * 131 + 1):
        # only keep track of the latest plots that are reached at each step
        curr, prev = get_new_plots(world, curr, prev), curr
        if k % 2 == 0:
            count_even += len(curr)
        else:
            count_odd += len(curr)

        if k % 131 == 65:
            F.append(count_even if k %2 == 0 else count_odd)

    assert len(F) == 3
    # we look for a degree 2 polynom F(x) = ax^2 + bx + c that fits
    fitted = polyfit([0, 1, 2], F, 2)
    a, b, c = round(fitted[2]), round(fitted[1]), round(fitted[0])
    return lambda x: a * x * x + b * x + c


def solve(world, start):
    F = find_quadratic_function(world, start)
    return F(202300)


if __name__ == "__main__":
    start = time.time()
    world, s_pos = parse("data.txt")
    result = solve(world, s_pos)
    print(f'Part 2 : {result}  ({round(1000 * (time.time() - start))} ms)')
