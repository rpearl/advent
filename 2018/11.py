from aocd import data, lines, submit
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math


def nosubmit(answer, part):
    print(f"Part {part}:\n{answer}")


submit = nosubmit


print(f"File line count: {len(lines)}")


def power(sn, x, y):
    rid = x + 10
    p = rid * y
    p += sn
    p *= rid
    p = (p // 100) % 10
    return p - 5


cgrid = defaultdict(int)
sn = int(data)
for y in range(300):
    s = 0
    for x in range(300):
        s += power(sn, x, y)
        cgrid[x, y] = cgrid[x, y - 1] + s


def region(sn, x, y, n=3):

    bottom = y + n - 1
    right = x + n - 1
    return (
        cgrid[right, bottom]
        - cgrid[x - 1, bottom]
        - cgrid[right, y - 1]
        + cgrid[x - 1, y - 1]
    )


def a():
    b = -math.inf
    bp = None
    sn = int(data)
    for x in range(300 - 3):
        for y in range(300 - 3):
            r = region(sn, x, y)
            if r > b:
                b = r
                bp = x, y
    x, y = bp
    return f"{x},{y}"


def b():
    br = -math.inf
    for size in range(1, 300):
        for x in range(300 - size):
            for y in range(300 - size):
                r = region(sn, x, y, size)
                if r > br:
                    b = x, y, size
                    br = r
    return ",".join(map(str, b))


def main():
    ra = a()
    if ra is not None:
        submit(ra, part="a")

    rb = b()
    if rb is not None:
        submit(rb, part="b")


main()
