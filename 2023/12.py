submit=True
from aocd import data #type: ignore
from aocd import submit as sbmt #type: ignore
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import re
import time
import operator
#data = """???.### 1,1,3"""
#data = "?###???????? 3,2,1"

_data="""???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

lines = data.splitlines()


ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

@functools.cache
def do_count(springs, si, counts, ci, count):
    if si == len(springs):
        return 1 if ci == len(counts) else 0

    if springs[si] == '#':
        return do_count(springs, si+1, counts, ci, count+1)

    elif springs[si] == '.' or ci == len(counts):
        if ci < len(counts) and counts[ci] == count:
            return do_count(springs, si+1, counts, ci+1, 0)
        elif count == 0:
            return do_count(springs, si+1, counts, ci, 0)
        else:
            return 0
    else:
        ret = do_count(springs, si+1, counts, ci, count+1)
        if count == counts[ci]:
            return ret + do_count(springs, si+1, counts, ci+1, 0)
        elif count == 0:
            return ret + do_count(springs, si+1, counts, ci, 0)
        else:
            return ret







def a():
    s = 0
    for line in lines:
        springs, counts = line.split(' ')
        counts = tuple(u.ints(counts))
        c = do_count(springs+'.', 0, counts, 0, 0)
        s += c
    return s


def b():
    s = 0
    for line in lines:
        springs, counts = line.split(' ')
        springs = '?'.join([springs]*5)
        counts = tuple(u.ints(counts)*5)
        c = do_count(springs+'.', 0, counts, 0, 0)
        s += c
    return s

def main():
    submit = globals().get('submit', False)
    astart = time.perf_counter()
    ra = a()
    aend = time.perf_counter()
    if ra is not None:
        print(f"Part a: {ra}")
        print(f"Time taken: {aend-astart:.4f} sec")
        if submit:
            sbmt(ra, part="a")

    bstart = time.perf_counter()
    rb = b()
    bend = time.perf_counter()
    if rb is not None:
        print(f"Part b: {rb}")
        print(f"Time taken: {bend-bstart:.4f} sec")
        if submit:
            sbmt(rb, part="b")
    print()
main()
