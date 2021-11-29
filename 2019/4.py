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

low, high = u.ints(data.replace("-", " "))
pws = [[(p // 10 ** (5 - e)) % 10 for e in range(6)] for p in range(low, high + 1)]


def asc(pw):
    return all(pw[i] <= pw[i + 1] for i in range(len(pw) - 1))


def group(p):
    return (len(list(g)) for _, g in itertools.groupby(p))


def nosubmit(answer, part):
    print(f"Part {part}:\n{answer}")


# submit = nosubmit

print(f"File line count: {len(lines)}")


def a():
    return sum(asc(pw) and any(g >= 2 for g in group(pw)) for pw in pws)


def b():
    return sum(asc(pw) and any(g == 2 for g in group(pw)) for pw in pws)


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
