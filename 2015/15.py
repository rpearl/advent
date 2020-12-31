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

properties = {}
calories = {}
all_ing = []

for line in lines:
    name, props = line.split(":")
    props = tuple(u.ints(props))
    properties[name] = props[:-1]
    calories[name] = props[-1]
    all_ing.append(name)


def a():
    def score(ingreds):
        s = [0] * 4
        for ing, qty in ingreds.items():
            props = properties[ing]
            for i in range(4):
                s[i] += qty * props[i]

        for i in range(4):
            s[i] = max(0, s[i])
        return math.prod(s)

    return max(
        score(Counter(combo))
        for combo in itertools.combinations_with_replacement(all_ing, 100)
    )


def b():
    def score(ingreds):
        s = [0] * 4
        cal = 0
        for ing, qty in ingreds.items():
            props = properties[ing]
            for i in range(4):
                s[i] += qty * props[i]
            cal += qty * calories[ing]
        if cal != 500:
            return 0
        for i in range(4):
            s[i] = max(0, s[i])
        return math.prod(s)

    return max(
        score(Counter(combo))
        for combo in itertools.combinations_with_replacement(all_ing, 100)
    )


u.main(a, b, submit=globals().get("submit", False))
