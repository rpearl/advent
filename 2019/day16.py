import itertools
import numpy as np
from math import ceil
import functools
from collections import defaultdict, namedtuple
import u
from aocd import data

inp = u.lmap(int, data)
ln = len(inp)


def pattern(i, ln):
    j = i + 1

    a = [0] * j
    b = [1] * j
    c = [0] * j
    d = [-1] * j
    v = a + b + c + d
    v1 = v[1:]
    return list(itertools.islice(itertools.chain(v1, itertools.cycle(v)), ln))


def mat(ln):
    return np.array([pattern(i, ln) for i in range(ln)])


def phase(mt, v):
    return np.mod(np.absolute(np.matmul(mt, v)), 10)


def a():
    m = mat(ln)
    val = np.array(inp)
    for _ in range(100):
        val = phase(m, val)

    return "".join(str(c) for c in val[:8])


def b():
    d = inp * 10_000
    offs = int("".join(str(c) for c in inp[:7]))
    d = d[offs:]
    for _ in range(100):
        partials = list(itertools.accumulate(d)):[-1]
        d = u.lmap(lambda p: (partials[-1] - p) % 10, partials)

    return "".join(str(x) for x in d[:8])


print(a())
print(b())  #
#
