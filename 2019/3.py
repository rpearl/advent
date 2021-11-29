from aocd import data, lines, submit
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator

deltas = {k: v for k, v in zip("LRDU", u.dirs)}

A, B = (line.split(",") for line in lines)


def get_points(cmds):
    x = 0
    y = 0

    out = {}
    length = 0
    for cmd in cmds:
        d = cmd[0]
        n = int(cmd[1:])

        dx, dy = deltas[d]
        for _ in range(n):
            x += dx
            y += dy
            length += 1
            if (x, y) not in out:
                out[(x, y)] = length
    return out


a_points = get_points(A)
b_points = get_points(B)

both = set(a_points.keys()) & set(b_points.keys())


def nosubmit(answer, part):
    print(f"Part {part}:\n{answer}")


# submit = nosubmit

print(f"File line count: {len(lines)}")


def a():
    return min(abs(x) + abs(y) for x, y in both)


def b():
    return min(a_points[p] + b_points[p] for p in both)


def main():
    astart = time.perf_counter()
    ra = a()
    aend = time.perf_counter()
    if ra is not None:
        print(ra)
        print(f"Time taken: {aend-astart:.4f} sec")
        submit(ra, part="a")

    bstart = time.perf_counter()
    rb = b()
    bend = time.perf_counter()
    if rb is not None:
        print(rb)
        print(f"Time taken: {bend-bstart:.4f} sec")
        submit(rb, part="b")


main()
