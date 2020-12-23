# submit=True
from aocd import data
import u
import itertools

items = set(u.ints(data))


def a():
    for x in items:
        y = 2020 - x
        if y in items:
            return x * y


def b():
    for x, y in itertools.combinations(items, 2):
        z = 2020 - x - y
        if z in items:
            return x * y * z


u.main(a, b, submit=globals().get("submit", False))
