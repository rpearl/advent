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
import re

runs = re.compile(
    "|".join(
        "".join(s)
        for s in zip(
            string.ascii_lowercase,
            string.ascii_lowercase[1:],
            string.ascii_lowercase[2:],
        )
    )
)

bs = {k: 26 - i for i, k in enumerate(string.ascii_lowercase)}


def powers(n):
    return map(pow, itertools.repeat(n), itertools.count())


def p2int(p):
    return sum(
        itertools.starmap(
            operator.mul, zip(powers(26), reversed([ord(k) - ord("a") for k in p]))
        )
    )


def int2p(n):
    if n < 26:
        return string.ascii_lowercase[n]
    else:
        q, r = divmod(n, 26)
        return int2p(q) + string.ascii_lowercase[r]


def has_run(pw):
    return runs.search(pw) is not None


pair = re.compile(r"([a-z])\1")


def has_pairs(pw):
    pairs = pair.findall(pw)
    return len(set(pairs)) >= 2


ambig = re.compile(r"[iol]")


def valid(pw):
    return has_run(pw) and has_pairs(pw) and ambig.search(pw) is None


def a():
    pw = data
    while not valid(pw):
        pw = int2p(p2int(pw) + 1)
    return pw


def b():
    pw = int2p(p2int(a()) + 1)
    while not valid(pw):
        pw = int2p(p2int(pw) + 1)
    return pw


u.main(a, b, submit=globals().get("submit", False))
