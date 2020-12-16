from aocd import lines, submit
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math


def nosubmit(answer, part):
    print(f"Part {part}:\n{answer}")


# submit = nosubmit

# data = """1, 1
# 1, 6
# 8, 3
# 3, 4
# 5, 5
# 8, 9"""
# lines = data.splitlines()


print(f"File line count: {len(lines)}")


def a():
    coords = [tuple(int(x.strip()) for x in line.split(",")) for line in lines]
    left = min(x for x, y in coords)
    right = max(x for x, y in coords)
    top = min(y for x, y in coords)
    bottom = max(y for x, y in coords)

    infs = set()

    closest = defaultdict(int)
    for x in range(left, right + 1):
        for y in range(top, bottom + 1):
            mn = math.inf
            c = None
            for i, (px, py) in enumerate(coords):
                d = abs(x - px) + abs(y - py)
                if d < mn:
                    c = i
                    mn = d
                elif d == mn:
                    c = None
            if x in {left, right} or y in {top, bottom}:
                closest[c] = math.inf
            else:
                closest[c] += 1
    return max(c for c in closest.values() if c < math.inf)


def b():
    coords = [tuple(int(x.strip()) for x in line.split(",")) for line in lines]
    left = min(x for x, y in coords)
    right = max(x for x, y in coords)
    top = min(y for x, y in coords)
    bottom = max(y for x, y in coords)

    region = 0
    for x in range(left, right + 1):
        for y in range(top, bottom + 1):
            tdist = 0
            for i, (px, py) in enumerate(coords):
                d = abs(x - px) + abs(y - py)
                tdist += d
            if tdist < 10000:
                region += 1
    return region


def main():
    ra = a()
    if ra is not None:
        submit(ra, part="a")

    rb = b()
    if rb is not None:
        submit(rb, part="b")


main()
