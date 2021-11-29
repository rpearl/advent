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


def nosubmit(answer, part):
    print(f"Part {part}:\n{answer}")


#submit = nosubmit

print(f"File line count: {len(lines)}")

def fuel(mass):
    return max(0, mass // 3 - 2)

def module_fuel(mass):
    tot = 0
    while mass > 0:
        f = fuel(mass)
        tot += f
        mass = f
    return tot

def a():
    return sum(map(fuel, u.ints(data)))


def b():
    return sum(map(module_fuel, u.ints(data)))


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
