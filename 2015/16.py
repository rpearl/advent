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

sues = {}
for line in lines:
    idx = line.index(":")
    sue, props = line[:idx], line[idx + 2 :]
    sue = sue[len("Sue ") :]
    kvs = [prop.split(": ") for prop in props.split(", ")]
    kvs = {k: int(v) for k, v in kvs}
    sues[int(sue)] = kvs

target = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def a():
    for sue, props in sues.items():
        if all(props[name] == target[name] for name in props):
            return sue
    pass


def b():
    ops = {
        "cats": operator.gt,
        "trees": operator.gt,
        "pomeranians": operator.lt,
        "goldfish": operator.lt,
    }
    for sue, props in sues.items():
        if all(ops.get(name, operator.eq)(props[name], target[name]) for name in props):
            return sue
    pass


u.main(a, b, submit=globals().get("submit", False))
