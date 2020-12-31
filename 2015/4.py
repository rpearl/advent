# submit=True
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
from hashlib import md5


def mine(n):
    s = "0" * n
    for i in itertools.count():
        if md5((data + str(i)).encode("ascii")).hexdigest().startswith(s):
            return i


def a():
    return mine(5)


def b():
    return mine(6)


u.main(a, b, submit=globals().get("submit", False))
