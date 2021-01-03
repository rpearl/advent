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

dirs = {
    "U": complex(0, -1),
    "D": complex(0, 1),
    "L": complex(-1, 0),
    "R": complex(1, 0),
}


def a():
    keys = {
        complex(x, y): c
        for y, row in enumerate(u.chunks(range(1, 10), 3))
        for x, c in enumerate(row)
    }

    def clamp(c):
        r = max(0, min(c.real, 2))
        i = max(0, min(c.imag, 2))
        return complex(r, i)

    code = []
    pos = complex(1, 1)
    for line in lines:
        for d in line:
            pos += dirs[d]
            pos = clamp(pos)
        code.append(str(keys[pos]))
    return "".join(code)


data2 = """ULL
RRDDD
LURDL
UUUUD"""
lines = data.splitlines()


def b():
    keys = {
        complex(0, -2): "1",
        complex(-1, -1): "2",
        complex(0, -1): "3",
        complex(1, -1): "4",
        complex(-2, 0): "5",
        complex(-1, 0): "6",
        complex(0, 0): "7",
        complex(1, 0): "8",
        complex(2, 0): "9",
        complex(-1, 1): "A",
        complex(0, 1): "B",
        complex(1, 1): "C",
        complex(0, 2): "D",
    }
    code = []
    pos = complex(-2, 0)
    for line in lines:
        for d in line:
            npos = pos + dirs[d]
            if npos in keys:
                pos = npos
        code.append(keys[pos])
    return "".join(code)
    pass


u.main(a, b, submit=globals().get("submit", False))
