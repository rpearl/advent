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


def tls(line):
    in_brackets = 0
    good = False
    for i, letter in enumerate(line[:-3]):
        if letter == "[":
            in_brackets += 1
        elif letter == "]":
            in_brackets -= 1
        else:
            abba = (
                letter == line[i + 3]
                and line[i + 1] == line[i + 2]
                and letter != line[i + 1]
            )
            if abba:
                if in_brackets == 0:
                    good = True
                else:
                    return False
    return good


def ssl(line):
    in_brackets = 0
    supernet = set()
    hypernet = set()
    for i, letter in enumerate(line[:-2]):
        if letter == "[":
            in_brackets += 1
        elif letter == "]":
            in_brackets -= 1
        else:
            aba = (
                letter == line[i + 2]
                and letter != line[i + 1]
                and line[i + 1] not in "[]"
            )
            if aba:
                s = line[i : i + 3]
                assert "]" not in s
                if in_brackets == 0:
                    supernet.add(s)
                else:
                    hypernet.add(s)
    for s in supernet:
        a, b, _ = s
        if b + a + b in hypernet:
            return True
    return False


print(ssl("zazbz[bzb]cdb"))
print(ssl("xyx[xyx]xyx"))
print(ssl("aba[bab]xyz"))


def a():
    return sum(tls(line) for line in lines)


def b():
    return sum(ssl(line) for line in lines)
    pass


u.main(a, b, submit=globals().get("submit", False))
