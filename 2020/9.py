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
        i, j = min(i,j),max(i,j)
        if sum_through[j] - sum_through[i] == target:
            subst = numbers[i:j]
            return min(subst) + max(subst)

    return s


def main():
    ra = a()
    if ra is not None:
        submit(ra, part="a")

    rb = b()
    if rb is not None:
        submit(rb, part="b")


main()
