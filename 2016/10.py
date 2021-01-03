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
import parse

p = parse.compile("bot {:d} gives low to {} {:d} and high to {} {:d}")


def a():
    instrs = {}
    bots = defaultdict(list)
    outputs = defaultdict(list)

    def put(typ, ident, val):
        if typ == "bot":
            bots[ident].append(val)
        else:
            outputs[ident].append(val)

    for line in lines:
        if line.startswith("value"):
            v, bot = u.ints(line)
            bots[bot].append(v)
        else:
            result = p.parse(line)
            bot, *rest = result.fixed
            assert bot not in instrs
            instrs[bot] = tuple(rest)

    while True:
        runnable = [bot for bot in bots if len(bots[bot]) == 2]
        for bot in runnable:
            vals = bots[bot]
            if len(vals) != 2:
                continue
            a, b = vals
            low = min(a, b)
            high = max(a, b)
            if (low, high) == (17, 61):
                return bot
            low_type, low_id, high_type, high_id = instrs[bot]
            put(low_type, low_id, low)
            put(high_type, high_id, high)
            bots[bot] = []


def b():
    instrs = {}
    bots = defaultdict(list)
    outputs = defaultdict(list)

    def put(typ, ident, val):
        if typ == "bot":
            bots[ident].append(val)
        else:
            outputs[ident].append(val)

    for line in lines:
        if line.startswith("value"):
            v, bot = u.ints(line)
            bots[bot].append(v)
        else:
            result = p.parse(line)
            bot, *rest = result.fixed
            assert bot not in instrs
            instrs[bot] = tuple(rest)

    while True:
        runnable = [bot for bot in bots if len(bots[bot]) == 2]
        for bot in runnable:
            vals = bots[bot]
            if len(vals) != 2:
                continue
            a, b = vals
            low = min(a, b)
            high = max(a, b)
            low_type, low_id, high_type, high_id = instrs[bot]
            put(low_type, low_id, low)
            put(high_type, high_id, high)
            bots[bot] = []
        if all(len(outputs[i]) > 0 for i in range(3)):
            print(outputs)
            return math.prod(outputs[i][0] for i in range(3))
    pass


u.main(a, b, submit=globals().get("submit", False))
