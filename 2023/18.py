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

_data="""R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""


lines = data.splitlines()

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def vadd(a, b):
    return (a[0]+b[0], a[1]+b[1])

def vmul(a, s):
    return (a[0]*s, a[1]*s)

dirs = {
    'U': u.N,
    'D': u.S,
    'L': u.W,
    'R': u.E,
}

def det(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    return x1*y2 - x2*y1

def a():
    points = [(0,0)]
    cur = points[-1]
    edges = 2
    for i, line in enumerate(lines):
        d, n, code = u.fixparse('{} {:d} (#{:x})', line)
        cur = vadd(cur, vmul(dirs[d], n))
        edges += n
        points.append(cur)

    s = edges
    for i in range(len(points)):
        s += det(points[i-1], points[i])

    return s // 2

def b():
    points = [(0,0)]
    cur = points[-1]
    edges = 2
    for i, line in enumerate(lines):
        code = u.fixparse('{} {:d} (#{})', line)[-1]
        n = int(code[:-1], 16)
        d = 'RDLU'[int(code[-1])]
        cur = vadd(cur, vmul(dirs[d], n))
        edges += n
        points.append(cur)



    s = edges
    for i in range(len(points)):
        s += det(points[i-1], points[i])

    return s // 2
    pass

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
