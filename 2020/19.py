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
from lark import Lark
import re


def a():
    rules, messages = data.split("\n\n")
    rules = re.sub(r"(\d+)", r"rule\1", rules)
    parser = Lark(rules, start="rule0")
    s = 0
    for line in messages.splitlines():
        try:
            parser.parse(line)
            s += 1
        except:
            pass
    return s


def b():
    rules, messages = data.split("\n\n")
    rules = rules.replace("8: 42", "8: 42 | 42 8")
    rules = rules.replace("11: 42 31", "11: 42 31 | 42 11 31")
    rules = re.sub(r"(\d+)", r"rule\1", rules)
    parser = Lark(rules, start="rule0")
    s = 0
    for line in messages.splitlines():
        try:
            parser.parse(line)
            s += 1
        except:
            pass
    return s
    pass


u.main(a, b, submit=globals().get("submit", False))
