submit=True
from aocd import data, lines #type: ignore
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator

_data="""Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

opmap = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}

class Monkey:
    def __init__(self, monkeys, items, lhs, op, rhs, test, c_true, c_false, div=True):
        self.monkeys=monkeys
        self.items = items
        self.lhs = lhs
        self.rhs = rhs
        self.op = op
        self.test = test
        self.c_true = c_true
        self.c_false = c_false
        self.count = 0
        self.div=div
        self.modulus = None
    def op_fn(self, old):
        l = old if self.lhs == 'old' else int(self.lhs)
        r = old if self.rhs == 'old' else int(self.rhs)
        val = self.op(l, r)
        if self.div:
            val = math.floor(val/3)
        else:
            val = val % self.modulus
        return val
    def throw_fn(self, worry):
        worry = self.op_fn(worry)
        self.count += 1
        if worry % self.test == 0:
            other = self.monkeys[self.c_true]
        else:
            other = self.monkeys[self.c_false]

        other.items.append(worry)

def a():
    chunks = [c.splitlines() for c in data.split('\n\n')]
    monkeys = []
    counts = []
    for monkey in chunks:
        starting_items = u.ints(monkey[1])
        op_string = monkey[2].split('=')[-1]
        lhs, op, rhs = op_string.split()
        op = opmap[op]

        test = u.ints(monkey[3])[0]
        c_true = u.ints(monkey[4])[0]
        c_false = u.ints(monkey[5])[0]
        monkeys.append(Monkey(monkeys=monkeys,items=starting_items, lhs=lhs, op=op, rhs=rhs , test=test,c_true=c_true,c_false=c_false))


    for _ in range(20):
        for i,monkey in enumerate(monkeys):
            for item in monkey.items:
                monkey.throw_fn(item)
            monkey.items.clear()

    counts = [monkey.count for monkey in monkeys]
    counts.sort()
    print(counts)
    return counts[-1]*counts[-2]



def b():
    chunks = [c.splitlines() for c in data.split('\n\n')]
    monkeys = []
    counts = []
    for monkey in chunks:
        starting_items = u.ints(monkey[1])
        op_string = monkey[2].split('=')[-1]
        lhs, op, rhs = op_string.split()
        op = opmap[op]

        test = u.ints(monkey[3])[0]
        c_true = u.ints(monkey[4])[0]
        c_false = u.ints(monkey[5])[0]
        monkeys.append(Monkey(monkeys=monkeys,items=starting_items, lhs=lhs, op=op, rhs=rhs , test=test,c_true=c_true,c_false=c_false,div=False))
    modulus = math.lcm(*[m.test for m in monkeys])
    for monkey in monkeys:
        monkey.modulus = modulus

    for _ in range(10000):
        for i,monkey in enumerate(monkeys):
            for item in monkey.items:
                monkey.throw_fn(item)
            monkey.items.clear()
    counts = [monkey.count for monkey in monkeys]
    counts.sort()
    print(counts)
    return counts[-1]*counts[-2]
    pass

u.main(a, b, submit=globals().get('submit', False))
