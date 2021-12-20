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

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def apply(remap, sign):
    def f(pts):
        return [
            (
                pt[remap[0]]*sign[0],
                pt[remap[1]]*sign[1],
                pt[remap[2]]*sign[2],
            ) for pt in pts
        ]
    return f

def subvec(v1, v2):
    return (v1[0]-v2[0], v1[1]-v2[1], v1[2]-v2[2])

def sqmagnitude(v):
    x,y,z = v
    return x**2 + y**2 + z**2

remap_p = [(0, 1, 2), (1, 2, 0), (2, 0, 1)]
sign_p = [(1, 1, 1), (-1, -1, 1), (-1, 1, -1), (1, -1, -1)]
remap_n = [(0, 2, 1), (1, 0, 2), (2, 1, 0)]
sign_n = [(-1, 1, 1), (1, -1, 1), (1, 1, -1), (-1, -1, -1)]
pos = itertools.product(remap_p, sign_p)
neg = itertools.product(remap_n, sign_n)
rotations = [apply(remap, sign) for remap, sign in itertools.chain(pos, neg)]

threshold = math.comb(12,2)

def align_scanners(scanner1, scanner2):
    for origin1 in scanner1:
        for rot in rotations:
            rscanner2 = rot(scanner2)
            for origin2 in rscanner2:
                delta = subvec(origin2, origin1)
                trscanner2 = {subvec(pt2, delta) for pt2 in rscanner2}
                if len(scanner1 & trscanner2) >= 12:
                    return True, delta, trscanner2
    return False, None, None


def fingerprint(scanner):
    return {sqmagnitude(subvec(*p)) for p in itertools.combinations(scanner, 2)}

def position_scanners():
    scanners = [set(u.chunks(u.ints(scanner)[1:], 3)) for scanner in data.split('\n\n')]
    fingerprints = u.lmap(fingerprint, scanners)

    positions = {0: (0,0,0)}
    relative_sensors = {0: scanners[0]}
    solvable = deque([0])
    while len(solvable) > 0:
        i = solvable.popleft()
        rscanner1 = relative_sensors[i]

        for j, scanner2 in enumerate(scanners):
            if j == i or j in positions or len(fingerprints[i] & fingerprints[j]) < threshold:
                continue
            aligned, position, rscanner2 = align_scanners(rscanner1, scanner2)
            if aligned:
                solvable.append(j)
                positions[j] = position
                relative_sensors[j] = rscanner2
    sensors = {pt for v in relative_sensors.values() for pt in v}
    return positions, sensors

def a():
    global positions
    global sensors
    positions, sensors = position_scanners()
    return len(sensors)

def manhattan(v1, v2):
    v = subvec(v1, v2)
    return abs(v[0]) + abs(v[1]) + abs(v[2])

def b():
    return max(manhattan(s1, s2) for s1, s2 in itertools.combinations(positions.values(), 2))

u.main(a, b, submit=globals().get('submit', False))
