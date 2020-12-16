from aocd import lines, submit
import sys
from collections import Counter, defaultdict, deque
import cachetools
import itertools
import u


def nosubmit(answer, part):
    print(f"Part {part}:\n{answer}")


# submit = nosubmit

# data = """bcde
# fghij
# klmno
# pqrst
# fguij
# axcye
# wvxyz"""
# lines = data.splitlines()


print(f"File numbers: {len(lines)}")


def a():
    twos = 0
    threes = 0
    for line in lines:
        c = Counter(line)
        if 2 in c.values():
            twos += 1
        if 3 in c.values():
            threes += 1
    return twos * threes


def b():
    d = defaultdict(list)
    for line in lines:
        for i in range(len(line)):
            candidate = line[:i] + line[i + 1 :]

            for other in d[candidate]:
                if len(other) == len(line) and other != line:
                    print(other)
                    print(line)
                    return candidate

            d[candidate].append(line)
    pass


def main():
    ra = a()
    if ra is not None:
        submit(ra, part="a")

    rb = b()
    if rb is not None:
        submit(rb, part="b")


main()
