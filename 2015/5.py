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
import re

vowels = set("aeiou")
bad = {"ab", "cd", "pq", "xy"}


def a():
    vowels = re.compile(r"[aeiou]")
    doubles = re.compile(r"(\w)\1")
    bad = re.compile(r"(ab)|(cd)|(pq)|(xy)")

    def nice(s):
        return (
            len(vowels.findall(s)) >= 3
            and bad.search(s) is None
            and doubles.search(s) is not None
        )

    return sum(nice(s) for s in lines)


def b():
    doubles = re.compile(r"(\w\w).*\1")
    repeats = re.compile(r"(\w).\1")

    def nice(s):
        return doubles.search(s) is not None and repeats.search(s) is not None

    return sum(nice(s) for s in lines)


u.main(a, b, submit=globals().get("submit", False))
