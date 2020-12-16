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


print(f"File line count: {len(lines)}")

# data = """Step C must be finished before step A can begin.
# Step C must be finished before step F can begin.
# Step A must be finished before step B can begin.
# Step A must be finished before step D can begin.
# Step B must be finished before step E can begin.
# Step D must be finished before step E can begin.
# Step F must be finished before step E can begin."""
#
# lines = data.splitlines()


def w(n):
    return ord(n) - 4


def a():
    g = defaultdict(set)
    gr = defaultdict(set)
    for line in lines:
        g[line[5]].add(line[36])
        gr[line[36]].add(line[5])
    s = SortedList(n for n in g.keys() if len(gr[n]) == 0)
    order = []

    while s:
        n = s.pop(0)
        order.append(n)
        edges = list(g[n])
        for m in edges:
            g[n].remove(m)
            gr[m].remove(n)
            if len(gr[m]) == 0:
                s.add(m)
    return "".join(order)


def b():
    g = defaultdict(set)
    gr = defaultdict(set)
    for line in lines:
        g[line[5]].add(line[36])
        gr[line[36]].add(line[5])

    workers = [0, 0, 0, 0, 0]
    s = SortedList((0, n) for n in g.keys() if len(gr[n]) == 0)
    order = SortedList([])

    while s:
        mtts, n = s.pop(0)
        mworker = None
        mw = math.inf
        for i, wt in enumerate(workers):
            if wt < mw:
                mworker = i
                mw = wt
        tts = max(mw, mtts)
        tte = tts + w(n)
        workers[mworker] = tte
        order.add((tte, n))
        edges = list(g[n])
        for m in edges:
            g[n].remove(m)
            gr[m].remove(n)
            if len(gr[m]) == 0:
                s.add((tte, m))
    return order[-1][0]


def main():
    ra = a()
    if ra is not None:
        submit(ra, part="a")

    rb = b()
    if rb is not None:
        submit(rb, part="b")


main()
