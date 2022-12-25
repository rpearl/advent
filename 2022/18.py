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

_data = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5"""
lines=data.splitlines()


ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

dirs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

def a():
    tot = 0
    cubes = set(tuple(p) for p in intlines)
    for x,y,z in intlines:
        for dx, dy, dz in dirs:
            nxt = (x+dx, y+dy, z+dz)
            if nxt not in cubes:
                tot += 1
    return tot

def vadd(a,b):
    return (a[0]+b[0], a[1]+b[1], a[2]+b[2])

def b():
    pts = set(tuple(p) for p in intlines)
    air = set()
    minx = min(p[0] for p in pts)-1
    miny = min(p[1] for p in pts)-1
    minz = min(p[2] for p in pts)-1
    maxx = max(p[0] for p in pts)+1
    maxy = max(p[1] for p in pts)+1
    maxz = max(p[2] for p in pts)+1
    minbound = (minx, miny, minz)
    maxbound = (maxx, maxy, maxz)
    print(minbound,maxbound)
    stack = [minbound]
    def inbounds(pt):
        return all(lo <= p <= hi for lo,p,hi in zip(minbound,pt,maxbound))
    while stack:
        cur = stack.pop()
        air.add(cur)
        for d in dirs:
            nxt = (cur[0]+d[0], cur[1]+d[1], cur[2]+d[2])
            if nxt not in pts and nxt not in air and inbounds(nxt):
                stack.append(nxt)

    total = 0
    for pt in pts:
        for d in dirs:
            if vadd(pt, d) in air:
                total += 1

    return total
    #cubes = set(tuple(p) for p in intlines)

    #air = set()
    #stack = [(minbound)]

    #while stack:
    #    cur = stack.pop()
    #    air.add(cur)
    #    for dx, dy, dz in dirs:
    #        nxt = (cur[0]+dx, cur[1]+dy, cur[2]+dz)
    #        if nxt not in cubes and nxt not in air and all(minbound[i] <= nxt[i] <= maxbound[i] for i in (0,1,2)):
    #            stack.append(nxt)
    #total = 0
    #for cube in cubes:
    #    for dx, dy, dz in dirs:
    #        nxt = (cur[0]+dx, cur[1]+dy, cur[2]+dz)
    #        if nxt in air:
    #            total += 1
    #return total



u.main(a, b, submit=globals().get('submit', False))
