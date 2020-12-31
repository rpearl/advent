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
import re
from lark import Lark, Visitor

data2 = """e => H
e => O
H => HO
H => OH
O => HH

HOHOHO"""

atoms = re.compile(r"[A-Z][a-z]?")


def atomize(s):
    return tuple(atoms.findall(s))


replacements = defaultdict(list)
rs, med = data.split("\n\n")
for line in rs.splitlines():
    src, dst = line.split(" => ")
    dst = atomize(dst)
    replacements[src].append(dst)
med = atomize(med)
# print(replacements)

# print(replacements)
print(med)


def reps(src):
    for i in range(len(src)):
        before, s, after = src[:i], src[i], src[i + 1 :]
        for rep in replacements[s]:
            yield before + rep + after


def a():
    seen = set()
    for rep in reps(med):
        seen.add(rep)

    return len(seen)


# print(repls)


def b():
    print(len(med))
    rn = med.count("Rn")
    ar = med.count("Ar")
    y = med.count("Y")
    return len(med) - rn - ar - 2 * y - 1


u.main(a, b, submit=globals().get("submit", False))
