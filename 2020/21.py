submit = True
from aocd import data, lines
import sys
from collections import Counter, defaultdict, deque, namedtuple
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator

print(f"File line count: {len(lines)}")


def a():
    allergens = defaultdict(Counter)
    ingred_to_allergens = defaultdict(set)
    mentions = Counter()
    for line in lines:
        ingreds, allerg = line.split(" (contains ")
        allerg = allerg[:-1].split(", ")
        ingreds = ingreds.split(" ")
        for al in allerg:
            allergens[al].update(ingreds)
        for ingred in ingreds:
            ingred_to_allergens[ingred] |= set(allerg)
        mentions.update(ingreds)

    res = []
    for ingred, als in ingred_to_allergens.items():
        if all(allergens[al][ingred] < max(allergens[al].values()) for al in als):
            res.append(ingred)

    return sum(mentions[ingred] for ingred in res)


def b():
    allergens = defaultdict(Counter)
    ingred_to_allergens = defaultdict(set)
    mentions = Counter()
    for line in lines:
        ingreds, allerg = line.split(" (contains ")
        allerg = allerg[:-1].split(", ")
        ingreds = ingreds.split(" ")
        for al in allerg:
            allergens[al].update(ingreds)
        for ingred in ingreds:
            ingred_to_allergens[ingred] |= set(allerg)
        mentions.update(ingreds)

    res = set()
    for ingred, als in ingred_to_allergens.items():
        if all(allergens[al][ingred] < max(allergens[al].values()) for al in als):
            res.add(ingred)

    for ingred in res:
        for al in ingred_to_allergens[ingred]:
            del allergens[al][ingred]
        del ingred_to_allergens[ingred]

    candidates = defaultdict(set)

    for al, counts in allergens.items():
        m = max(counts.values())
        candidates[al] = set(ingred for ingred, c in counts.items() if c == m)
    print(candidates)

    assigned = dict()
    while len(assigned) < len(candidates):
        to_clear = set()
        for al, possible in candidates.items():
            if len(possible) == 1:
                p = possible.pop()
                assigned[al] = p
                to_clear.add(p)
        for al, c in candidates.items():
            c -= to_clear

    out = []
    for al in sorted(assigned.keys()):
        out.append(assigned[al])
    return ",".join(out)


u.main(a, b, submit=globals().get("submit", False))
