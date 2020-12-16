from aocd import lines, submit
import sys
from collections import Counter, defaultdict, deque
import cachetools
import itertools
import u


def nosubmit(answer, part):
    print(f"Part {part}:\n{answer}")


# submit = nosubmit


print(f"File line count: {len(lines)}")


def a():
    claimed = Counter()
    for line in lines:
        _, _, lt, wh = line.split(" ")
        lt = lt[:-1]
        l, t = [int(x) for x in lt.split(",")]
        w, h = [int(x) for x in wh.split("x")]

        for i in range(l, l + w):
            for j in range(t, t + h):
                claimed[(i, j)] += 1

    return len([v for v in claimed.values() if v > 1])

    pass


def b():
    claimed = Counter()
    claims = {}
    for line in lines:
        ident, _, lt, wh = line.split(" ")
        lt = lt[:-1]
        l, t = [int(x) for x in lt.split(",")]
        w, h = [int(x) for x in wh.split("x")]
        claims[ident] = (l, t, w, h)

    for ident, (l, t, w, h) in claims.items():
        for i in range(l, l + w):
            for j in range(t, t + h):
                claimed[(i, j)] += 1

    for ident, (l, t, w, h) in claims.items():
        if all(claimed[(i, j)] == 1 for i in range(l, l + w) for j in range(t, t + h)):
            return ident[1:]


def main():
    ra = a()
    if ra is not None:
        submit(ra, part="a")

    rb = b()
    if rb is not None:
        submit(rb, part="b")


main()
