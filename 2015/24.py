submit = True
from aocd import data, lines
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator
from libnum import factorize


def a():
    packages = list(reversed(sorted(u.ints(data))))
    target = sum(packages) // 3

    for k in range(4, len(packages)):
        for subset in itertools.combinations(packages, k):
            if sum(subset) == target:
                return math.prod(subset)


def b():
    packages = list(reversed(sorted(u.ints(data))))
    target = sum(packages) // 4

    for k in range(2, len(packages)):
        for subset in itertools.combinations(packages, k):
            if sum(subset) == target:
                return math.prod(subset)
    pass


u.main(a, b, submit=globals().get("submit", False))
