#!/usr/bin/env python3
import re
import time


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Brick:
    def __init__(self, id, start, end):
        self.id = id
        self.start = start
        self.end = end
        self.carried_by = set()
        self.carry = set()


def parse(input_path):
    with open(input_path, 'r') as f:
        bricks = []
        for (i, line) in enumerate(f.readlines()):
            x1, y1, z1, x2, y2 ,z2 = re.findall(r'\d+', line)
            bricks.append(Brick(i, Point3D(int(x1), int(y1), int(z1)), Point3D(int(x2), int(y2), int(z2))))
        return bricks


def get_lowest_reachable_z(brick1, brick2):
    x_overlap = brick2.start.x <= brick1.start.x <= brick2.end.x \
             or brick1.start.x <= brick2.start.x <= brick1.end.x
    y_overlap = brick2.start.y <= brick1.start.y <= brick2.end.y \
             or brick1.start.y <= brick2.start.y <= brick1.end.y
    return 1 if not x_overlap or not y_overlap else brick2.end.z + 1  # one step above brick2


def get_stable_state(flying_bricks):
    flying_bricks = sorted(flying_bricks, key=lambda brick: brick.start.z)  # sort from lowest to highest z
    bricks = {}
    for flying_brick in flying_bricks:
        target_z = 1
        carried_by = []
        for brick_id in bricks:
            lowest_z = get_lowest_reachable_z(flying_brick, bricks[brick_id])
            if lowest_z > target_z:
                target_z = lowest_z
                carried_by = {brick_id}
            elif lowest_z == target_z and target_z != 1:
                carried_by.add(brick_id)
        shift = flying_brick.start.z - target_z
        shifted_brick = Brick(flying_brick.id,
                              Point3D(flying_brick.start.x, flying_brick.start.y, flying_brick.start.z - shift),
                              Point3D(flying_brick.end.x,   flying_brick.end.y,   flying_brick.end.z - shift))
        shifted_brick.carried_by = carried_by
        for carrier_id in carried_by:
            bricks[carrier_id].carry.add(shifted_brick.id)
        bricks[shifted_brick.id] = shifted_brick
    return bricks


def solve(bricks):
    bricks = get_stable_state(bricks)
    # a brick can be disintegrated if all bricks it carries have at least another carrier
    return len([1 for brick_id in bricks
                if all([len(bricks[supported_brick].carried_by) > 1 for supported_brick in bricks[brick_id].carry])])


if __name__ == "__main__":
    start = time.time()
    bricks = parse("data.txt")
    result = solve(bricks)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
