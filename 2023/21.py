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

lines = data.splitlines()

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def a():
    grid = {}
    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            grid[x,y] = c if c != 'S' else '.'
            if c == 'S':
                start = (x,y)

    seen = { start }
    results = []
    for s in range(64):
        newseen = set()
        for point in seen:
            for d in u.dirs:
                px, py = point
                dx, dy = d
                np = px+dx, py+dy
                if grid.get(np) == '.':
                    newseen.add(np)
        seen = newseen
    return len(seen)


def b():
    grid = {}
    w = len(lines[0])
    h = len(lines)
    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            grid[x,y] = c if c != 'S' else '.'
            if c == 'S':
                start = (x,y)

    steps = 26501365

    seen = { start }
    results = []
    for s in range(steps):
        newseen = set()
        for point in seen:
            for d in u.dirs:
                px, py = point
                dx, dy = d
                nx, ny = px+dx, py+dy
                if grid.get((nx % w, ny % h)) == '.':
                    newseen.add((nx, ny))

        if s % w == steps % w:
            print(s, len(seen), s // w)
            results.append(len(seen))
        seen = newseen

        if len(results) == 3:
            break


    iters = steps // w
    b0 = results[0]
    b1 = results[1]-results[0]
    b2 = (results[2]-2*results[1] + results[0]) // 2
    return b0 + b1*iters + iters*(iters-1)*b2


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
