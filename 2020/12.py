# submit = True
from aocd import lines, data
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
from u import N, S, E, W
import math


def rotv(v, deg):
    nturns = deg % 360
    x, y = v
    for i in range(nturns // 90):
        x, y = -y, x
    return [x, y]


def a():
    pos = [0, 0]
    wp = (1, 0)

    for a in lines:
        n = int(a[1:])
        if a[0] == "F":
            pos[0] += wp[0] * n
            pos[1] += wp[1] * n
        elif a[0] == "N":
            pos[0] += N[0] * n
            pos[1] += N[1] * n
        elif a[0] == "S":
            pos[0] += S[0] * n
            pos[1] += S[1] * n
        elif a[0] == "E":
            pos[0] += E[0] * n
            pos[1] += E[1] * n
        elif a[0] == "W":
            pos[0] += W[0] * n
            pos[1] += W[1] * n
        elif a[0] == "L":
            wp = rotv(wp, n)
        elif a[0] == "R":
            wp = rotv(wp, -n)
    return sum(abs(x) for x in pos)


def b():
    pos = [0, 0]
    wp = [10, 1]

    for a in lines:
        n = int(a[1:])
        if a[0] == "F":
            pos[0] += wp[0] * n
            pos[1] += wp[1] * n
        elif a[0] == "N":
            wp[0] += N[0] * n
            wp[1] += N[1] * n
        elif a[0] == "S":
            wp[0] += S[0] * n
            wp[1] += S[1] * n
        elif a[0] == "E":
            wp[0] += E[0] * n
            wp[1] += E[1] * n
        elif a[0] == "W":
            wp[0] += W[0] * n
            wp[1] += W[1] * n
        elif a[0] == "L":
            wp = rotv(wp, n)
        elif a[0] == "R":
            wp = rotv(wp, -n)
    return sum(abs(x) for x in pos)
    pass


u.main(a, b, submit=globals().get("submit", False))
