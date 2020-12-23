submit = True
from aocd import data, lines
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import operator


def a():
    groups = data.split("\n\n")
    criteria, ticket, nearby = [l.split("\n") for l in groups]

    rules = {}

    for c in criteria:
        k, vs = c.split(":")
        rs = u.lmap(tuple, u.chunks(u.ints(vs.replace("-", " to ")), 2))
        rules[k] = rs

    def valid(val):
        for ruleset in rules.values():
            for a, b in ruleset:
                if a <= val <= b:
                    return True
        return False

    s = 0
    for ticket in nearby[1:]:
        t = u.ints(ticket)
        for v in t:
            if not valid(v):
                s += v
    return s


def b():
    groups = data.split("\n\n")
    criteria, my_ticket, nearby = [g.split("\n") for g in groups]
    my_ticket = u.ints(my_ticket[1])

    rules = {}

    for c in criteria:
        k, vs = c.split(":")
        rs = u.lmap(tuple, u.chunks(u.ints(vs.replace("-", " ")), 2))
        rules[k] = rs

    def valid_for_field(v, field):
        return any(a <= v <= b for a, b in rules[field])

    def valid(val):
        return any(valid_for_field(val, field) for field in rules)

    valid_nearby = []

    for ticket in nearby[1:]:
        t = u.ints(ticket)
        if all(valid(v) for v in t):
            valid_nearby.append(t)

    possible = []
    for _ in range(len(my_ticket)):
        possible.append(set(rules.keys()))

    for ticket in valid_nearby:
        for i, v in enumerate(ticket):
            pl = list(possible[i])
            for field in pl:
                if not valid_for_field(v, field):
                    possible[i].remove(field)

    mapping = {}
    allocated = set()
    for i, p in sorted(enumerate(possible), key=lambda x: x[1]):
        field = (p - allocated).pop()
        mapping[i] = field
        allocated.add(field)

    s = functools.reduce(
        operator.mul,
        (my_ticket[i] for i in mapping if mapping[i].startswith("departure")),
        1,
    )
    return s


u.main(a, b, submit=globals().get("submit", False))
