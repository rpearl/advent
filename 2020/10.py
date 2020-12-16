from aocd import data, submit
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


# print(f"File line count: {len(lines)}")

# data = """16
# 10
# 15
# 5
# 1
# 11
# 7
# 19
# 6
# 12
# 4"""

# data = """28
# 33
# 18
# 42
# 31
# 14
# 46
# 20
# 48
# 47
# 24
# 23
# 49
# 45
# 19
# 38
# 39
# 11
# 1
# 32
# 25
# 35
# 8
# 17
# 7
# 9
# 4
# 2
# 34
# 10
# 3"""


def a():
    adapters = [0] + list(sorted(int(line) for line in data.split("\n")))
    adapters.append(adapters[-1] + 3)
    diffs = Counter(adapters[i] - adapters[i - 1] for i in range(1, len(adapters)))
    return diffs[3] * diffs[1]


def b():
    adapters = [int(line) for line in data.split("\n")]
    adapters.sort()
    adapters.append(adapters[-1] + 3)
    outputs = []

    ways = Counter({0: 1})
    for jolt in adapters:
        ways[jolt] = ways[jolt - 1] + ways[jolt - 2] + ways[jolt - 3]
    return ways[adapters[-1]]


def main():
    ra = a()
    if ra is not None:
        submit(ra, part="a")

    rb = b()
    if rb is not None:
        submit(rb, part="b")


main()
