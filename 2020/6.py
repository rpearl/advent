submit = True
from aocd import data
from collections import Counter
import itertools
import u


def a():
    s = 0
    for grp in data.split("\n\n"):
        counts = Counter()
        counts.update(itertools.chain.from_iterable(grp.splitlines()))
        s += len(counts.keys())
    return s


def b():
    s = 0
    for grp in data.split("\n\n"):
        counts = Counter()
        ppl = grp.splitlines()
        counts.update(itertools.chain.from_iterable(ppl))
        s += list(counts.values()).count(len(ppl))
    return s


u.main(a, b, submit=globals().get("submit", False))
