submit = True
from aocd import data, lines
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math


def a():
    mask = 0
    mem = defaultdict(int)
    for line in lines:
        if line.startswith("mask"):
            mask = line.split("=")[1].strip()
            ors = int(mask.replace("X", "0"), 2)
            ands = int(mask.replace("X", "1"), 2)
        else:
            m, v = u.ints(line)
            mem[m] = (v | ors) & ands
    return sum(mem.values())
    pass


def addrs(mask, addr):
    astr = [c if m == "0" else m for c, m in zip(bin(addr)[2:].zfill(36), mask)]
    indexes = [((i, "0"), (i, "1")) for i, x in enumerate(astr) if x == "X"]
    floating = itertools.product(*indexes)

    for change in floating:
        m = list(astr)
        for i, v in change:
            m[i] = v
        yield int("".join(m), 2)


def b():
    mask = 0
    mem = defaultdict(int)
    for line in lines:
        if line.startswith("mask"):
            mask = line.split("=")[1].strip()
        else:
            m, v = u.ints(line)
            for addr in addrs(mask, m):
                mem[addr] = v
    return sum(mem.values())


u.main(a, b, submit=globals().get("submit", False))
