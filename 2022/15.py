submit=True
from aocd import data, lines #type: ignore
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator
import z3

#data = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
#Sensor at x=9, y=16: closest beacon is at x=10, y=16
#Sensor at x=13, y=2: closest beacon is at x=15, y=3
#Sensor at x=12, y=14: closest beacon is at x=10, y=16
#Sensor at x=10, y=20: closest beacon is at x=10, y=16
#Sensor at x=14, y=17: closest beacon is at x=10, y=16
#Sensor at x=8, y=7: closest beacon is at x=2, y=10
#Sensor at x=2, y=0: closest beacon is at x=2, y=10
#Sensor at x=0, y=11: closest beacon is at x=2, y=10
#Sensor at x=20, y=14: closest beacon is at x=25, y=17
#Sensor at x=17, y=20: closest beacon is at x=21, y=22
#Sensor at x=16, y=7: closest beacon is at x=15, y=3
#Sensor at x=14, y=3: closest beacon is at x=15, y=3
#Sensor at x=20, y=1: closest beacon is at x=15, y=3"""
#lines = data.splitlines()

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]


#target_y = 10
target_y = 2000000

def mdist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x2-x1) + abs(y2-y1)
sensors = {}
beacons = set()
for sx, sy, bx, by in intlines:
    s = sx, sy
    b = bx, by
    sensors[s] = mdist(s, b)
    beacons.add(b)

def size(rng):
    lo, hi = rng
    return hi-lo+1


def a():
    visible = set()
    for sensor, bdist in sensors.items():
        sx, sy = sensor
        dist_to_target_y = mdist((sx, target_y), sensor)
        remaining = bdist - dist_to_target_y + 1
        for dx in range(remaining):
            visible.add((sx+dx, target_y))
            visible.add((sx-dx, target_y))

    return len(visible) - sum(1 for b in beacons if b[1] == target_y)


def b():
    x = z3.Int('x')
    y = z3.Int('y')
    def z3Abs(u):
        return z3.If(u > 0, u, -u)

    def z3DistTo(p1, p2):
        return z3Abs(p1[0] - p2[0]) + z3Abs(p1[1] - p2[1])

    s = z3.Solver()
    s.add(0 <= x)
    s.add(x <= 4000000)
    s.add(0 <= y)
    s.add(y <= 4000000)

    for sensor, bdist in sensors.items():
        s.add(z3DistTo(sensor, (x,y)) > bdist)

    s.check()
    m = s.model()
    return m[x].as_long()*4000000+m[y].as_long()

u.main(a, b, submit=globals().get('submit', False))
