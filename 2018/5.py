from aocd import data, lines, submit
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u


def nosubmit(answer, part):
    print(f"Part {part}:\n{answer}")


submit = nosubmit


print(f"File line count: {len(lines)}")

# data = "dabAcCaCBAcCcaDA"


def react(start):
    st = list(start + " ")
    n = []
    changed = True

    while changed:
        n = []
        changed = False
        i = 0
        while i < len(st) - 1:
            l, r = st[i : i + 2]
            if l.islower() != r.islower() and l.lower() == r.lower():
                i += 2
                changed = True
            else:
                n.append(l)
                i += 1
        n.append(st[-1])
        if not changed:
            return st[:-1]
        st = list(n)


def a():
    return len(react(data))


def b():
    partial = "".join(react(data))
    cs = set(partial.lower())
    best = min(len(react(partial.replace(c, "").replace(c.upper(), ""))) for c in cs)
    return best


def main():
    ra = a()
    if ra is not None:
        submit(ra, part="a")

    rb = b()
    if rb is not None:
        submit(rb, part="b")


main()
