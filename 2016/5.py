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
import hashlib


def a():
    pass
    out = []
    i = 0
    while len(out) < 8:
        d = (data + str(i)).encode("ascii")
        h = hashlib.md5(d).hexdigest()
        if h.startswith("0" * 5):
            out.append(h[5])
        i += 1
    return "".join(out)
    pass


def b():
    out = [None] * 8
    c = 0
    i = 0
    while c < 8:
        d = (data + str(i)).encode("ascii")
        h = hashlib.md5(d).hexdigest()
        p = h[5]
        if h.startswith("0" * 5) and "0" <= p < "8":
            p = int(p)
            if out[p] == None:
                out[p] = h[6]
                c += 1
        i += 1
    return "".join(out)
    pass


u.main(a, b, submit=globals().get("submit", False))
