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


def a():
    p1, p2 = data.split("\n\n")
    cards1 = deque(map(int, p1.splitlines()[1:]))
    cards2 = deque(map(int, p2.splitlines()[1:]))

    while len(cards1) and len(cards2):
        c1 = cards1.popleft()
        c2 = cards2.popleft()
        if c1 > c2:
            cards1.extend([c1, c2])
        else:
            cards2.extend([c2, c1])

    deck = cards1 if len(cards1) else cards2
    return sum((len(deck) - i) * c for i, c in enumerate(deck))


def play_game(*cards, subgame=False):
    if subgame and max(cards[0]) > max(cards[1]):
        return 0
    seen = set()
    while cards[0] and cards[1]:
        key = tuple(map(tuple, cards))
        if key in seen:
            return 0
        else:
            draw0 = cards[0].pop(0)
            draw1 = cards[1].pop(0)
            if len(cards[0]) >= draw0 and len(cards[1]) >= draw1:
                subdeck0 = cards[0][:draw0]
                subdeck1 = cards[1][:draw1]
                winner = play_game(subdeck0, subdeck1, subgame=True)
            else:
                winner = draw1 > draw0
        seen.add(key)
        draw = draw0, draw1
        cards[winner].extend([draw[winner], draw[1 - winner]])

    return 0 if len(cards[0]) else 1


def b():
    p1, p2 = data.split("\n\n")
    cards1 = list(map(int, p1.splitlines()[1:]))
    cards2 = list(map(int, p2.splitlines()[1:]))

    play_game(cards1, cards2)
    deck = cards1 if len(cards1) else cards2
    return sum((len(deck) - i) * c for i, c in enumerate(deck))


u.main(a, b, submit=globals().get("submit", False))
