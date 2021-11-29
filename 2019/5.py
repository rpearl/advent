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
import intcode


def nosubmit(answer, part):
    print(f"Part {part}:\n{answer}")


# submit = nosubmit

print(f"File line count: {len(lines)}")


def a():
    outs = list(intcode.run(data, [1]))
    if all(v == 0 for v in outs[:-1]):
        return outs[-1]
    pass


def b():
    outs = list(intcode.run(data, [5]))
    if all(v == 0 for v in outs[:-1]):
        return outs[-1]


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
