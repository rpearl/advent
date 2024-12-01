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

#data = """3   4
#4   3
#2   5
#1   3
#3   9
#3   3"""

lines = data.splitlines()

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def a():
    lefts,rights = zip(*intlines)
    #lefts = []
    #rights = []
    #for a,b in intlines:
    #    lefts.append(a)
    #    rights.append(b)
    s = 0
    return sum(abs(a-b) for a,b in zip(sorted(lefts), sorted(rights)))
    pass


def b():
    lefts,rights = zip(*intlines)
    #lefts = []
    #rights = []
    #for a,b in intlines:
    #    lefts.append(a)
    #    rights.append(b)

    rights = Counter(rights)
    return sum(a*rights[a] for a in lefts)

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
