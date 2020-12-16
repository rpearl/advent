from aocd import data, lines, submit
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u


def nosubmit(answer, part):
    print(f"Part {part}:\n{answer}")


# submit = nosubmit


print(f"File line count: {len(lines)}")

# data = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"

d = [int(x) for x in data.split(" ")]


def parse():
    i = 0

    def read():
        nonlocal i
        o = d[i]
        i += 1
        return o

    def _parse():
        nc = read()
        nm = read()
        children = tuple(_parse() for _ in range(nc))
        metadata = tuple(read() for _ in range(nm))
        return (children, metadata)

    return _parse()


tree = parse()


def a():
    def check(node):
        children, metadata = node
        return sum(check(child) for child in children) + sum(metadata)

    return check(tree)


def b():
    @functools.cache
    def value(node):
        children, metadata = node
        if not children:
            return sum(metadata)
        else:
            s = 0
            for idx in metadata:
                if 0 <= idx - 1 < len(children):
                    s += value(children[idx - 1])
            return s

    return value(tree)


def main():
    ra = a()
    if ra is not None:
        submit(ra, part="a")

    rb = b()
    if rb is not None:
        submit(rb, part="b")


main()
