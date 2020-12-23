submit = True
from aocd import data, lines
import sys
from collections import Counter, defaultdict, deque, namedtuple
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator

# data = "389125467"


def run(cards, rounds):
    cups = [int(c) for c in data]
    m = max(cups)
    cups.extend(x + 1 for x in range(m, cards))
    m = cards

    nxt = [None] * (m + 1)
    head = None
    tail = None
    for c in cups:
        if not head:
            head = c
        if tail:
            nxt[tail] = c
        tail = c
    nxt[tail] = head
    cur = head
    for _ in range(rounds):
        p1 = nxt[cur]
        p2 = nxt[p1]
        p3 = nxt[p2]
        nxt[cur] = nxt[p3]

        label = cur
        while True:
            label -= 1
            if label == 0:
                label = m
            if label != p1 and label != p2 and label != p3:
                break

        nxt[p3] = nxt[label]
        nxt[label] = p1
        cur = nxt[cur]

    return nxt


def a():
    nxt = run(len(data), 100)
    ptr = nxt[1]
    out = []
    while ptr != 1:
        out.append(str(ptr))
        ptr = nxt[ptr]
    return "".join(out)


def b():
    nxt = run(1_000_000, 10_000_000)
    n = nxt[1]
    return n * nxt[n]


u.main(a, b, submit=globals().get("submit", False))
