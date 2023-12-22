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
import time
import operator

_data="""broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""

lines = data.splitlines()

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]


modules = {}
modules['button'] = ('@', ['broadcaster'], None)
inputs = defaultdict(set)
for line in lines:
    src, dests = line.split(' -> ')
    dests = dests.split(', ')
    if src[0] in '%&':
        typ, src = src[0], src[1:]
    else:
        typ = '@'
        state = None
    if typ == '%':
        state = [False]
    elif typ == '&':
        state = {}
    modules[src] = (typ, dests, state)
    for dest in dests:
        inputs[dest].add(src)


def a():
    for name, (typ, _, state) in modules.items():
        if typ == '&':
            for src in inputs[name]:
                state[src] = False
        elif typ == '%':
            state[0] = False
    counts = Counter()

    for _ in range(1000):
        queue = deque([('button', False, None)])
        while queue:
            (cur, pulse, src) = queue.pop()
            if cur not in modules:
                continue
            typ, dests, state = modules[cur]
            npulse = None
            if typ == '@':
                npulse = pulse
            elif typ == '%' and pulse == False:
                state[0] = not state[0]
                npulse = state[0]
            elif typ == '&':
                state[src] = pulse
                npulse = not all(state.values())

            if npulse is not None:
                for dest in dests:
                    queue.appendleft((dest, npulse, cur))
                counts[npulse] += len(dests)
    return math.prod(counts.values())


def b():
    for name, (typ, _, state) in modules.items():
        if typ == '&':
            for src in inputs[name]:
                state[src] = False
        elif typ == '%':
            state[0] = False


    # this only works for aoc inputs and not in general.
    # where we have &A -> rx
    # and a number of &B, &C, &D that hook up to &A directly.
    # these all cycle independently but there doesn't seem to be a fundamental reason why
    to_watch = inputs[list(inputs['rx'])[0]]
    cycles = []

    queue = deque()
    for step in itertools.count(1):
        queue.appendleft(('button', False, None))
        while queue:
            (cur, pulse, src) = queue.pop()
            if cur in to_watch and not pulse:
                if pulse == False:
                    cycles.append(step)
                if len(cycles) == len(to_watch):
                    r = 1
                    for v in cycles:
                        r = u.lcm(r, v)
                    return r

            if cur not in modules:
                continue
            typ, dests, state = modules[cur]
            npulse = None
            if typ == '@':
                npulse = pulse
            elif typ == '%' and pulse == False:
                state[0] = not state[0]
                npulse = state[0]
            elif typ == '&':
                state[src] = pulse
                npulse = not all(state.values())

            if npulse is not None:
                for dest in dests:
                    queue.appendleft((dest, npulse, cur))

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
