import itertools
import math
from collections import defaultdict
from functools import reduce
from aocd import lines
import u


def lcms(numbers):
    return reduce(u.lcm, numbers)


def simulate(positions, velocities, max_steps=math.inf):
    op, ov = list(positions), list(velocities)
    step = 0
    while step < max_steps and (step == 0 or positions != op or velocities != ov):
        for i in range(len(positions)):
            velocities[i] += sum(
                1 if positions[i] < position else -1
                for position in positions
                if positions[i] != position
            )
        for i in range(len(positions)):
            positions[i] += velocities[i]
        step += 1
    return step


def a():
    positions = u.lmap(u.ints, lines)

    px, vx = [p[0] for p in positions], [0] * len(positions)
    py, vy = [p[1] for p in positions], [0] * len(positions)
    pz, vz = [p[2] for p in positions], [0] * len(positions)

    simulate(px, vx, 1000)
    simulate(py, vy, 1000)
    simulate(pz, vz, 1000)

    return sum(
        (abs(px[i]) + abs(py[i]) + abs(pz[i])) * (abs(vx[i]) + abs(vy[i]) + abs(vz[i]))
        for i in range(len(positions))
    )


def b():
    positions = u.lmap(u.ints, lines)
    px, vx = [p[0] for p in positions], [0] * len(positions)
    py, vy = [p[1] for p in positions], [0] * len(positions)
    pz, vz = [p[2] for p in positions], [0] * len(positions)

    sx = simulate(px, vx)
    sy = simulate(py, vy)
    sz = simulate(pz, vz)

    return lcms((sx, sy, sz))


u.main(a, b, submit=globals().get("submit", False))
