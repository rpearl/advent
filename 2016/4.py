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
import string


def a():
    s = 0
    for line in lines:
        l = line.split("-")
        ename, meta = l[:-1], l[-1]
        sector, csum = meta[:-1].split("[")
        sector = int(sector)
        counter = Counter(sorted("".join(ename)))
        expected = "".join(c for c, _ in counter.most_common(5))
        if expected == csum:
            s += sector
    return s


def b():
    real = []
    for line in lines:
        l = line.split("-")
        ename, meta = l[:-1], l[-1]
        sector, csum = meta[:-1].split("[")
        sector = int(sector)
        counter = Counter(sorted("".join(ename)))
        expected = "".join(c for c, _ in counter.most_common(5))
        if expected == csum:
            real.append((ename, sector))
    for ename, sector in real:
        tr = []
        for i, letter in enumerate(string.ascii_lowercase):
            tr.append(
                string.ascii_lowercase[(i + sector) % len(string.ascii_lowercase)]
            )
        table = str.maketrans(string.ascii_lowercase, "".join(tr))
        name = " ".join(ename).translate(table)
        if name.startswith("northpole"):
            return sector
    pass


u.main(a, b, submit=globals().get("submit", False))
