submit = True
import operator
import sys
from itertools import permutations
from collections import defaultdict
import intcode
from aocd import data
import u


def a():
    (out,) = intcode.run(data, [1])
    return out


def b():
    (out,) = intcode.run(data, [2])
    return out


u.main(a, b, submit=globals().get("submit", False))
