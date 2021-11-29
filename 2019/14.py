submit = True
import itertools
from math import ceil
import functools
from collections import defaultdict, namedtuple
import sys
from aocd import lines
import u

# 10 ORE => 10 A
# 1 ORE => 1 B
# 7 A, 1 B => 1 C
# 7 A, 1 C => 1 D
# 7 A, 1 D => 1 E
# 7 A, 1 E => 1 FUEL

Reaction = namedtuple("Reaction", ["product", "qty", "reactants"])

reactions = {}
for line in lines:
    i, o = [c.strip() for c in line.split(" => ")]
    inps = [c.split(" ") for c in i.split(", ")]
    inps = [(int(a), b) for a, b in inps]
    outs = [c.split(" ") for c in o.split(", ")]
    outs = [(int(a), b) for a, b in outs]

    for qty, chem in outs:
        reactions[chem] = Reaction(product=chem, qty=qty, reactants=inps)


def ore_per_fuel(fuel=1):
    required = defaultdict(int, {"FUEL": fuel})

    stack = [reactions["FUEL"]]

    while stack:
        reaction = stack.pop()
        needed = ceil(required[reaction.product] / reaction.qty)

        for qty, chem in reaction.reactants:
            required[chem] += needed * qty

            precursor = reactions.get(chem)
            if precursor is not None:
                stack.append(precursor)

        required[reaction.product] -= needed * reaction.qty

    return required["ORE"]


def a():
    return ore_per_fuel()


def b():
    low = 1
    high = 1e12
    used = 1e12

    while high > low:
        mid = int((low + high) / 2)
        if mid == low:
            break
        ore = ore_per_fuel(fuel=mid)
        if ore == used:
            return mid
        if ore > used:
            high = mid
        else:
            low = mid
    return mid


u.main(a, b, submit=globals().get("submit", False))
