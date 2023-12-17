#submit=True
from aocd import data #type: ignore
from aocd import submit as sbmt #type: ignore
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator

_data="""Time:      7  15   30
Distance:  9  40  200"""

lines = data.splitlines()

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

# x ms at 0 + (total-x) ms at x > record



def a():

    def count_ways(record, total_ms):
        ways = 0
        for i in range(1, total_ms):
            if i*(total_ms-i) > record:
                ways += 1
        return ways

    times, distances = [u.ints(l) for l in lines]

    ways = [count_ways(record, total_ms) for record, total_ms in zip(distances, times)]
    return math.prod(ways)

    pass


def b():
    def count_ways(record, total_ms):
        ways = 0
        for i in range(1, total_ms):
            if i*(total_ms-i) > record:
                ways += 1
        return ways

    time = int(lines[0].split(':')[1].replace(' ', ''))
    distance = int(lines[1].split(':')[1].replace(' ', ''))
    return count_ways(distance, time)

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
