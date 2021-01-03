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


def a():
    pos = 0
    d = u.N
    for instr in data.split(", "):
        turn, blocks = instr[0], int(instr[1:])
        if turn == "R":
            d = u.rot90[d]
        else:
            d = u.rot90[u.rot90[u.rot90[d]]]
        pos += blocks * complex(*d)
    return int(abs(pos.real)) + int(abs(pos.imag))


def b():
    pos = 0
    seen = {pos}
    d = u.N
    for instr in data.split(", "):
        turn, blocks = instr[0], int(instr[1:])
        if turn == "R":
            d = u.rot90[d]
        else:
            d = u.rot90[u.rot90[u.rot90[d]]]
        for _ in range(blocks):
            pos += complex(*d)
            if pos in seen:
                return int(abs(pos.real)) + int(abs(pos.imag))
            seen.add(pos)


u.main(a, b, submit=globals().get("submit", False))
