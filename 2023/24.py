submit=True
from aocd import data #type: ignore
from aocd import submit as sbmt #type: ignore
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator
import numpy as np
import z3


#data="""19, 13, 30 @ -2,  1, -2
#18, 19, 22 @ -1, -1, -2
#20, 25, 34 @ -2, -2, -4
#12, 31, 28 @ -1, -2, -1
#20, 19, 15 @  1, -5, -3"""

lines = data.splitlines()

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def intersection(A, B, C, D):
    a1 = B[1] - A[1]
    b1 = A[0] - B[0]
    c1 = a1 * (A[0]) + b1 * (A[1])

    a2 = D[1] - C[1]
    b2 = C[0] - D[0]
    c2 = a2 * (C[0]) + b2 * (C[1])

    det = a1 * b2 - a2 * b1

    if det == 0:
        return (float('inf'), float('inf'))

    x = ((b2 * c1) - (b1 * c2)) / det
    y = ((a1 * c2) - (a2 * c1)) / det
    return (x, y)


def a():
    stones = [u.lmap(tuple, u.chunks(line, 3)) for line in intlines]
    if len(stones) < 10:
        lo = 7
        hi = 27
    else:
        lo = 200000000000000
        hi = 400000000000000

    s = 0

    for stone1, stone2 in itertools.combinations(stones, 2):
        p1, v1 = stone1
        p2, v2 = stone2
        Ax = p1[0] + v1[0]*lo
        Ay = p1[1] + v1[1]*lo
        Bx = p1[0] + v1[0]*hi
        By = p1[1] + v1[1]*hi

        Cx = p2[0] + v2[0]*lo
        Cy = p2[1] + v2[1]*lo
        Dx = p2[0] + v2[0]*hi
        Dy = p2[1] + v2[1]*hi

        A = (Ax,Ay)
        B = (Bx,By)
        C = (Cx,Cy)
        D = (Dx,Dy)

        ix, iy = intersection(A,B,C,D)

        # ix = Ax + v1x * t
        # (ix - Ax) / v1x

        t1 = (ix - p1[0]) / v1[0]
        t2 = (ix - p2[0]) / v2[0]
        if t1 >= 0 and t2 >= 0 and lo <= ix <= hi and lo <= iy <= hi:
            s += 1
    return s


def b():
    stones = [u.lmap(tuple, u.chunks(line, 3)) for line in intlines]
    s = z3.Solver()

    throw_x = z3.Real('x')
    throw_y = z3.Real('y')
    throw_z = z3.Real('z')

    throw_vx = z3.Real('vx')
    throw_vy = z3.Real('vy')
    throw_vz = z3.Real('vz')

    # throw_x + throw_vx * t0 == p0 + 

    for i,stone in enumerate(stones[:3]):
        pos, vel = stone
        t = z3.Real(f't{i}')
        s.add(throw_x + throw_vx * t == pos[0] + vel[0] * t)
        s.add(throw_y + throw_vy * t == pos[1] + vel[1] * t)
        s.add(throw_z + throw_vz * t == pos[2] + vel[2] * t)

    s.check()
    m = s.model()
    return m[throw_x].as_long() + m[throw_y].as_long() + m[throw_z].as_long()


def main():
    submit = globals().get('submit', False)
    astart = time.perf_counter()
    ra = a()
    aend = time.perf_counter()
    if ra is not None:
        print(f"Part a: {ra}")
        print(f"Time taken: {aend-astart:.4f} sec")
        if submit:
            sbmt(ra, part="a")

    bstart = time.perf_counter()
    rb = b()
    bend = time.perf_counter()
    if rb is not None:
        print(f"Part b: {rb}")
        print(f"Time taken: {bend-bstart:.4f} sec")
        if submit:
            sbmt(rb, part="b")
    print()
main()
