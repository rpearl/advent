submit = True
from aocd import numbers
import sys
from collections import Counter, defaultdict, deque
import cachetools
import itertools
import u


def a():
    for i, l in enumerate(numbers[25:]):
        if not any(
            l == numbers[j] + numbers[k]
            for j, k in itertools.combinations(range(i, i + 25), 2)
        ):
            return l


def b():
    target = a()
    c = len(numbers)

    sum_through = list(itertools.accumulate(numbers))

    for i, j in itertools.combinations(range(c), 2):
        if sum_through[j] - sum_through[i] == target:
            subst = numbers[i:j]
            return min(subst) + max(subst)

    return s


u.main(a, b, submit=globals().get("submit", False))
