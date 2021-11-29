submit = True
from math import atan2, pi, hypot
import sys
from collections import defaultdict
from aocd import lines
import u

asteroids = []
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "#":
            asteroids.append((x, y))


def angle(p1, p2):
    p1x, p1y = p1
    p2x, p2y = p2
    return (pi / 2 + atan2(p2y - p1y, p2x - p1x)) % (2 * pi)


def angles(p1, asteroids):
    angles = defaultdict(list)
    for p2 in asteroids:
        angles[angle(p1, p2)].append(p2)
    return angles


def a():
    best = 0
    for asteroid in asteroids:
        a = angles(asteroid, asteroids)
        c = len(a)
        if c > best:
            best = c
    return best


def b():
    best = 0
    besta = None
    bestp = None
    for asteroid in asteroids:
        a = angles(asteroid, asteroids)
        c = len(a)
        if c > best:
            best = c
            besta = a
            bestp = asteroid

    for k, v in besta.items():
        v.sort(key=lambda p: hypot(p[0] - bestp[0], p[1] - bestp[1]))

    order = list(sorted(besta.keys()))
    for i in range(199):
        k = order[i % len(order)]
        p = besta[k].pop()
    x, y = besta[order[199 % len(order)]][-1]
    return x * 100 + y


u.main(a, b, submit=globals().get("submit", False))
