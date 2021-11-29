# submit = True
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

# data = ".^^.^.^^^^"
N = len(data)


def step(row):
    nr = []
    for i in range(N):
        left = False if i == 0 else row[i - 1]
        right = False if i == N - 1 else row[i + 1]
        nr.append(left ^ right)
    return nr


def print_row(row):
    print("".join("^" if row[i] else "." for i in range(len(row))))


def count(steps):
    row = [c == "^" for c in data]
    count = 0
    for _ in range(steps):
        count += sum(row)
        row = step(row)
    return N * steps - count


def a():
    return count(40)


def b():
    return count(400_000)


u.main(a, b, submit=globals().get("submit", False))
