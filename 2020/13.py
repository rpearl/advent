from aocd import data, lines, submit
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
from libnum import solve_crt

from functools import reduce



def nosubmit(answer, part):
    print(f"Part {part}:\n{answer}")


# submit = nosubmit


print(f"File line count: {len(lines)}")

# data = """939
# 7,13,x,x,59,x,31,19"""
# lines = data.splitlines()


def a():
    ts = int(lines[0])
    ids = u.ints(lines[1])

    best = math.inf
    bi = None

    for b in ids:
        earliest = math.ceil(ts / b) * b
        l = earliest - ts
        if l < best:
            best = l
            bi = b
    return bi * best

    pass


def b():
    ids = lines[1].split(",")

    return solve_crt([-i for i, x in enumerate(ids) if x != "x"],
        [int(x) for x in ids if x != "x"], 
    )
    pass


def main():
    ra = a()
    if ra is not None:
        submit(ra, part="a")

    rb = b()
    if rb is not None:
        submit(rb, part="b")


main()
