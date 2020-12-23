submit = True
from aocd import data
import sys
import operator
from sortedcontainers import SortedList, SortedSet, SortedDict
from collections import Counter, defaultdict, deque
import functools
import itertools
import u


def nosubmit(answer, part):
    print(f"Part {part}:\n{answer}")


submit = nosubmit


def a():
    adapters = [0] + sorted(u.ints(data))
    adapters.append(adapters[-1] + 3)
    diffs = Counter(adapters[i] - adapters[i - 1] for i in range(1, len(adapters)))
    return diffs[3] * diffs[1]


def b():
    adapters = u.ints(data)
    adapters.sort()
    adapters.append(adapters[-1] + 3)
    outputs = []

    ways = Counter({0: 1})
    for jolt in adapters:
        ways[jolt] = ways[jolt - 1] + ways[jolt - 2] + ways[jolt - 3]
    return ways[adapters[-1]]


u.main(a, b, submit=globals().get("submit", False))
