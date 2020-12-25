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


def find_loop(target0, target1):
    val = 1
    i = 0
    while val != target0 and val != target1:
        i += 1
        val *= 7
        val %= 20201227
    if val == target0:
        return 0, i
    else:
        return 1, i


def a():
    pks = u.ints(data)

    i, loop = find_loop(*pks)
    subj = pks[1 - i]
    val = 1

    val = pow(subj, loop, 20201227)
    return val


def b():
    pass


u.main(a, b, submit=globals().get("submit", False))
