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


def index(row, col):
    c = (row - 1) + col
    v = c * (c + 1) // 2
    return v - row + 1


print("    |" + " ".join(f" {i:2} " for i in range(1, 7)))
print("----+" + "+".join(f"----" for i in range(1, 7)))
for r in range(1, 7):
    rr = []
    for c in range(1, 8 - r):
        rr.append(index(r, c))
    print(f" {r:2} |" + " ".join(f" {i:2} " for i in rr))


def code(row, col):
    return (20151125 * pow(252533, index(row, col) - 1, 33554393)) % 33554393


print()
print("   |" + " ".join(f"{i:9}" for i in range(1, 7)))
print("---+" + "+".join(f"----------" for i in range(1, 7)))
for r in range(1, 7):
    rr = []
    for c in range(1, 7):
        rr.append(code(r, c))
    print(f" {r:1} |" + " ".join(f" {i:8} " for i in rr))


def a():
    row, col = u.ints(data)
    return code(row, col)


def b():
    pass


u.main(a, b, submit=globals().get("submit", False))
