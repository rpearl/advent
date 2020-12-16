from aocd import numbers, submit
import sys
from collections import Counter, defaultdict, deque
import cachetools
import itertools
import u


def nosubmit(answer, part):
    print(f"Part {part}:\n{answer}")


submit = nosubmit


print(f"File numbers: {len(numbers)}")


def a():
    return sum(numbers)


def b():
    s = 0
    seen = set([s])
    for n in itertools.cycle(numbers):
        s += n
        if s in seen:
            return s
        seen.add(s)


def main():
    ra = a()
    if ra is not None:
        submit(ra, part="a")

    rb = b()
    if rb is not None:
        submit(rb, part="b")


main()
