submit = True
from aocd import data, lines
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator

weapons = [
    ("Dagger", 8, 4, 0),
    ("Shortsword", 10, 5, 0),
    ("Warhammer", 25, 6, 0),
    ("Longsword", 40, 7, 0),
    ("Greataxe", 74, 8, 0),
]
armors = [
    ("no armor", 0, 0, 0),
    ("Leather", 13, 0, 1),
    ("Chainmail", 31, 0, 2),
    ("Splintmail", 53, 0, 3),
    ("Bandedmail", 75, 0, 4),
    ("Platemail", 102, 0, 5),
]

rings = [
    ("Nothing", 0, 0, 0),
    ("Damage +1", 25, 1, 0),
    ("Damage +2", 50, 2, 0),
    ("Damage +3", 100, 3, 0),
    ("Defense +1", 20, 0, 1),
    ("Defense +2", 40, 0, 2),
    ("Defense +3", 80, 0, 3),
]


def items():
    for its in itertools.product(weapons, armors, rings, rings):
        w, a, r1, r2 = its
        if r1 == r2 and r1 != rings[0]:
            continue
        yield its


def a():
    def fight_cost(items, player_hp=100):
        boss_hp, boss_damage, boss_armor = u.ints(data)
        cost = sum(item[1] for item in items)
        damage = sum(item[2] for item in items)
        armor = sum(item[3] for item in items)
        necessary_hits = boss_hp // max(damage - boss_armor, 1)
        my_damage = (necessary_hits - 1) * max(boss_damage - armor, 1)
        if my_damage < player_hp:
            return cost
        else:
            return math.inf

    return min(fight_cost(items) for items in items())


def b():
    def fight_cost(items, player_hp=100):
        boss_hp, boss_damage, boss_armor = u.ints(data)
        cost = sum(item[1] for item in items)
        damage = sum(item[2] for item in items)
        armor = sum(item[3] for item in items)
        necessary_hits = boss_hp // max(damage - boss_armor, 1)
        my_damage = (necessary_hits - 1) * max(boss_damage - armor, 1)
        if my_damage < player_hp:
            return -math.inf
        else:
            return cost

    return max(fight_cost(items) for items in items())
    pass


u.main(a, b, submit=globals().get("submit", False))
