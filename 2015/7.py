# submit = True
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

data2 = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i"""
lines = data.splitlines()


def a():
    wires = {}
    ops = {
        "LSHIFT": operator.lshift,
        "RSHIFT": operator.rshift,
        "OR": operator.or_,
        "AND": operator.and_,
    }

    for line in lines:
        gate, dest = line.split(" -> ")
        gate = gate.split(" ")
        if len(gate) == 1:
            wires[dest] = (lambda x: x, [gate[0]])
        elif len(gate) == 2:
            wires[dest] = (operator.inv, [gate[1]])
        else:
            x, op, y = gate
            wires[dest] = (ops[op], [x, y])

    @functools.cache
    def compute(node):
        if node.isdigit():
            return int(node)
        vs = []
        op, deps = wires[node]
        for dep in wires[node][1]:
            if not dep.isdigit():
                v = compute(dep)
            else:
                v = int(dep)
            vs.append(v)
        return op(*vs)

    return compute("a")


def b():
    wires = {}
    ops = {
        "LSHIFT": operator.lshift,
        "RSHIFT": operator.rshift,
        "OR": operator.or_,
        "AND": operator.and_,
    }

    for line in lines:
        gate, dest = line.split(" -> ")
        gate = gate.split(" ")
        if len(gate) == 1:
            wires[dest] = (lambda x: x, [gate[0]])
        elif len(gate) == 2:
            wires[dest] = (operator.inv, [gate[1]])
        else:
            x, op, y = gate
            wires[dest] = (ops[op], [x, y])

    wires["b"] = (lambda x: x, [str(a())])

    @functools.cache
    def compute(node):
        if node.isdigit():
            return int(node)
        vs = []
        op, deps = wires[node]
        for dep in wires[node][1]:
            if not dep.isdigit():
                v = compute(dep)
            else:
                v = int(dep)
            vs.append(v)
        return op(*vs)

    return compute("a")


u.main(a, b, submit=globals().get("submit", False))
