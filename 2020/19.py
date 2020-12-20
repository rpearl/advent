from aocd import data, lines, submit
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


def nosubmit(answer, part):
    print(f"Part {part}:\n{answer}")


submit = nosubmit

print(f"File line count: {len(lines)}")


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


def main():
    astart = time.perf_counter()
    ra = a()
    aend = time.perf_counter()
    if ra is not None:
        print(ra)
        print(f"Time taken: {aend-astart:.4f} sec")
        submit(ra, part="a")

    bstart = time.perf_counter()
    rb = b()
    bend = time.perf_counter()
    if rb is not None:
        print(rb)
        print(f"Time taken: {bend-bstart:.4f} sec")
        submit(rb, part="b")


main()