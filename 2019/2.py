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


def evaluate(noun, verb):
    mem = defaultdict(int, enumerate([int(v) for v in data.split(",")]))
    mem[1] = noun
    mem[2] = verb

    for _ in intcode.run(mem, []):
        pass

    return mem[0]


def a():
    return evaluate(12, 2)


def b():
    for noun in range(99):
        for verb in range(99):
            try:
                result = evaluate(noun, verb)
                if result == 19690720:
                    return 100 * noun + verb
            except Exception:
                pass


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
