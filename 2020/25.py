submit = True
from aocd import numbers
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator


def a():
    card, loop = numbers
    val = 1
    i = 0
    while True:
        i += 1
        val *= 7
        val %= 20201227
        if val == card:
            subj = loop
            break
        elif val == loop:
            subj = card
            break
    return pow(subj, i, 20201227)


def b():
    pass


u.main(a, b, submit=globals().get("submit", False))
