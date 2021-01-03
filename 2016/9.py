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


def decompress(s):
    out = []
    i = 0
    while i < len(s):
        c = s[i]
        if c == "(":
            end = s.find(")", i)
            marker = s[i:end]
            l, rpt = u.ints(marker)
            val = s[end + 1 : end + 1 + l]
            out.append(val * rpt)
            i = end + l
        else:
            out.append(c)
        i += 1
    return "".join(out)


# print(decompress("ADVENT"))
# print(decompress("A(1x5)BC"))
# print(decompress("(3x3)XYZ"))
# print(decompress("A(2x2)BCD(2x2)EFG"))
# print(decompress("X(8x2)(3x3)ABCY"))


def a():
    length = 0
    i = 0
    s = data
    while i < len(s):
        c = s[i]
        if c == "(":
            end = s.find(")", i)
            marker = s[i:end]
            l, rpt = u.ints(marker)
            val = s[end + 1 : end + 1 + l]
            length += len(val) * rpt
            i = end + l
        else:
            length += 1
        i += 1
    return length


def b():
    def find_length(s):
        length = 0
        i = 0
        while i < len(s):
            c = s[i]
            if c == "(":
                end = s.find(")", i)
                marker = s[i:end]
                l, rpt = u.ints(marker)
                val = s[end + 1 : end + 1 + l]
                tot = find_length(val)
                length += tot * rpt
                i = end + l
            else:
                length += 1
            i += 1
        return length

    return find_length(data)


u.main(a, b, submit=globals().get("submit", False))
