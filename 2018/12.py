from aocd import data, lines, submit
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math


def nosubmit(answer, part):
    print(f"Part {part}:\n{answer}")


# submit = nosubmit

# data = """initial state: #..#.#..##......###...###
#
# ...## => #
# ..#.. => #
# .#... => #
# .#.#. => #
# .#.## => #
# .##.. => #
# .#### => #
##.#.# => #
##.### => #
###.#. => #
###.## => #
####.. => #
####.# => #
#####. => #"""
# lines = data.splitlines()

print(f"File line count: {len(lines)}")


def a():
    initial = lines[0].split(":")[1].strip()
    rules = lines[2:]
    rules = {tuple(rule[:5]): rule[-1] for rule in rules}
    # print(rules)

    state = {i: x for i, x in enumerate(initial)}
    for step in range(20):
        print(f"{step:2}:" + "".join(state.get(i, ".") for i in range(-3, 36)))
        left = min(state.keys())
        right = max(state.keys())
        nstate = {}
        for i in range(left - 2, right + 3):
            rule = tuple(state.get(i + d, ".") for d in range(-2, 3))
            # if step == 0 and i == -1:
            #    print(rule, rules.get(rule, "."))
            nstate[i] = rules.get(rule, ".")
        state = nstate
    return sum(i for i in state.keys() if state[i] == "#")
    pass


def b():
    initial = lines[0].split(":")[1].strip()
    rules = lines[2:]
    rules = {tuple(rule[:5]): rule[-1] for rule in rules}
    # print(rules)

    state = {i: x for i, x in enumerate(initial)}
    step = 0
    print("b")
    while True:
        left = min(state.keys())
        right = max(state.keys())
        if step == 100:
            s = 50 * (50000000000 - step) + sum(
                i for i in state.keys() if state[i] == "#"
            )
            return s
            # count -= 1
            # print(f"{step:2}:" + "".join(state.get(i, ".") for i in range(left, right)))
        step += 1
        nstate = {}
        for i in range(left - 2, right + 3):
            rule = tuple(state.get(i + d, ".") for d in range(-2, 3))
            # if step == 0 and i == -1:
            #    print(rule, rules.get(rule, "."))
            nstate[i] = rules.get(rule, ".")
        state = nstate

    pass


def main():
    ra = a()
    if ra is not None:
        submit(ra, part="a")

    rb = b()
    if rb is not None:
        submit(rb, part="b")


main()
