from aocd import data, lines, submit
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math

_submit = submit


def nosubmit(answer, part):
    print(f"Part {part}:\n{answer}")

def submit(answer, part):
    nosubmit(answer, part)
    _submit(answer, part)


#submit = nosubmit


print(f"File line count: {len(lines)}")

#data = "0,3,6"


def a():
    d = {}
    hist = u.ints(data)
    for i,x in enumerate(hist[:-1]):
        d[x] = i
    while len(hist) < 2020:
        last = hist[-1]
        idx = len(hist) - 1
        prev = d.get(last, idx)
        hist.append(idx - prev)
        d[last] = idx
    return hist[2020-1]


def b():
    d = {}
    hist = u.ints(data)
    for i,x in enumerate(hist[:-1]):
        d[x] = i
    while len(hist) < 30000000:
        last = hist[-1]
        idx = len(hist) - 1
        prev = d.get(last, idx)
        hist.append(idx - prev)
        d[last] = idx
    return hist[30000000-1]


def main():
    ra = a()
    if ra is not None:
        submit(ra, part="a")

    rb = b()
    if rb is not None:
        submit(rb, part="b")


main()
