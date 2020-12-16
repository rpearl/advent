from aocd import data, lines, submit
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math


def nosubmit(answer, part):
    print(f"Part {part}:\n{answer}")


# submit = nosubmit


print(f"File line count: {len(lines)}")

# data = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
# mem[8] = 11
# mem[7] = 101
# mem[8] = 0"""
# lines = data.splitlines()

# data = """mask = 000000000000000000000000000000X1001X
# mem[42] = 100
# mask = 00000000000000000000000000000000X0XX
# mem[26] = 1"""
# lines = data.splitlines()


def a():
    mask = 0
    mem = defaultdict(int)
    for line in lines:
        if line.startswith("mask"):
            mask = line.split("=")[1].strip()
            ors = int(mask.replace("X", "0"), 2)
            # force off everything that's a 0:
            ands = int(mask.replace("X", "1"), 2)
        else:
            m, v = u.ints(line)
            # print(m, v, (v | ors) & ands)
            mem[m] = (v | ors) & ands
    return sum(mem.values())
    pass


def addrs(mask, addr):
    astr = [c if m == "0" else m for c, m in zip(bin(addr)[2:].zfill(36), mask)]
    indexes = [((i, '0'), (i, '1')) for i, x in enumerate(astr) if x == "X"]
    floating = itertools.product(*indexes) #"01", repeat=len(indexes))

    for change in floating:
        m = list(astr)
        for i, v in change:
            m[i] = v
        yield int("".join(m), 2)


def b():
    mask = 0
    mem = defaultdict(int)
    for line in lines:
        if line.startswith("mask"):
            mask = line.split("=")[1].strip()
        else:
            m, v = u.ints(line)
            for addr in addrs(mask, m):
                mem[addr] = v
    return sum(mem.values())


def main():
    ra = a()
    if ra is not None:
        submit(ra, part="a")

    rb = b()
    if rb is not None:
        submit(rb, part="b")


main()
