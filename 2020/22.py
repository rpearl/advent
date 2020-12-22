from aocd import data, lines, submit
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator


def nosubmit(answer, part):
    print(f"Part {part}:\n{answer}")


data2 = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""
# submit = nosubmit

print(f"File line count: {len(lines)}")


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


def play_game(*cards):
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
                winner = play_game(subdeck0, subdeck1)
            else:
                winner = 0 if draw0 > draw1 else 1
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


def main():
    astart = time.perf_counter()
    ra = a()
    aend = time.perf_counter()
    if ra is not None:
        print(ra)
        print(f"Time taken: {aend-astart:.4f} sec")
        submit(ra, part="a")

    bstart = time.perf_counter()
    rb = b()
    bend = time.perf_counter()
    if rb is not None:
        print(rb)
        print(f"Time taken: {bend-bstart:.4f} sec")
        submit(rb, part="b")


main()
