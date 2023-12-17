#submit=True
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


_data = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""
lines = data.splitlines()

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def vadd(p1, p2):
    return (p1[0]+p2[0], p1[1]+p2[1])

def a():
    grid, width, height = u.make_grid(lines, func=lambda p,_:int(p))
    def neighbors(node):
        pos, d = node
        d1 = u.rot90[d]
        d2 = u.rot90[u.rot90[u.rot90[d]]]
        for d in [d1, d2]:
            w = 0
            for i in range(3):
                npos = (pos[0] + d[0]*(i+1), pos[1] + d[1]*(i+1))
                if npos in grid:
                    w += grid[npos]
                    yield ((npos, d), w)

    start = [
        ((0,0), u.S),
        ((0,0), u.E)
    ]
    target = (width-1, height-1)
    _, dists = u.dijkstra(start, neighbors)
    return min(dists[target, d] for d in [u.N, u.S, u.E, u.W])



def b():
    grid, width, height = u.make_grid(lines, func=lambda p,_:int(p))
    def neighbors(node):
        pos, d = node
        d1 = u.rot90[d]
        d2 = u.rot90[u.rot90[u.rot90[d]]]

        for d in [d1, d2]:
            w = 0
            for count in range(1, 10+1):
                npos = (pos[0] + d[0]*count, pos[1] + d[1]*count)
                if npos in grid:
                    w += grid[npos]
                    if count >= 4:
                        yield ((npos, d), w)

    starts = [
        ((0,0), u.S),
        ((0,0), u.E),
    ]
    target = (width-1, height-1)
    _, dists = u.dijkstra(
        starts,
        neighbors,
    )
    return min(dists[target, d] for d in [u.N, u.S, u.E, u.W])

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
