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

data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

#lines = data.splitlines()
#
#ints = u.ints(data)
#intlines = u.lmap(u.ints, lines)
#toklines = [line.split(' ') for line in lines]


def lookup(m, i):
    for d, s, n in m:
        if s <= i < s + n:
            return d + (i - s)
    return i

def ilookup(m, i):
    for d, s, n in m:
        if d <= i < d + n:
            return s + (i - d)
    return i

descs = ['soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']

@functools.cache
def get_upper_bound():
    chunks = [c.rstrip('\n').split('\n') for c in data.split('\n\n')]
    seeds = u.ints(chunks[0][0])
    maps =[]
    nums=[]
    for lines in chunks[1:]:
        m = [u.ints(s) for s in lines[1:] if s]
        maps.append(m)

    for seed in seeds:
        for i,m in enumerate(maps):
            seed = lookup(m, seed)
        nums.append(seed)
    return min(nums)

def a():
    return get_upper_bound()


def b():
    ub = get_upper_bound()
    print(f'{ub=}')
    chunks = [c.rstrip('\n').split('\n') for c in data.split('\n\n')]
    seed_ranges = u.chunks(u.ints(chunks[0][0]), 2)
    def is_seed(val):
        for s, ln in seed_ranges:
            print(f'{s=} {val=} {s+ln=}')
            if s <= val < s+ln:
                return True
        return False

    maps =[]
    for lines in chunks[1:]:
        m = [u.ints(s) for s in lines[1:] if s]
        maps.append(m)

    for loc in range(ub):
        if loc % 10000 == 0:
            print(f"{loc=}")
        cur = loc
        for m in reversed(maps):
            cur = ilookup(m, cur)
        if is_seed(cur):
            return cur

    pass

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
