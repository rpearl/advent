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
import json

# data = """[1,{"c":"red","b":2},3]"""


def a():
    return sum(u.ints(data))


def jsonsum(obj):
    s = 0
    t = type(obj)
    if t == list:
        return sum(jsonsum(item) for item in obj)
    elif t == int:
        return obj
    elif t == str:
        return 0
    else:
        s = 0
        for v in obj.values():
            if v == "red":
                return 0
            s += jsonsum(v)
        return s


def b():
    d = json.loads(data)
    return jsonsum(d)


u.main(a, b, submit=globals().get("submit", False))
