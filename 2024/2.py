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

_data="""7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

lines = data.splitlines()

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def is_safe(ints):
    sign = u.sign(ints[0] - ints[1])
    safe = True
    for i, x in enumerate(ints[:-1]):
        d = ints[i] - ints[i+1]
        if not (1 <= abs(d)  <= 3 and u.sign(d) == sign):
            safe = False
            break
    return safe

def a():
    s = 0
    for line in lines:
        if is_safe(u.ints(line)): s += 1
    return s
    pass


def b():
    s = 0
    for line in lines:
        ints = u.ints(line)
        if is_safe(ints) or any(is_safe(ints[0:i]+ints[i+1:]) for i in range(len(ints))):
            s += 1
    return s
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
