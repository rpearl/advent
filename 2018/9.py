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


print(f"File line count: {len(lines)}")

# data = "9 players; last marble is worth 25 points"
# data = "10 players; last marble is worth 1618 points"
# data = "13 players; last marble is worth 7999 points"


def a():
    players, last = u.ints(data)

    scores = Counter()

    marbles = u.Linked(0)
    st = marbles
    player = 0

    for marble in range(1, last + 1):
        if marble % 23 == 0:
            scores[player] += marble
            other = marbles.move(-7)
            scores[player] += other.item
            marbles = other.move(1)
            other.remove()
        else:
            cur = u.Linked(marble)
            marbles.move(1).add(cur)
            marbles = cur
        player = (player + 1) % players

    return max(scores.values())


def b():
    players, last = u.ints(data)
    last *= 100

    scores = Counter()

    marbles = u.Linked(0)
    st = marbles
    player = 0

    for marble in range(1, last + 1):
        if marble % 23 == 0:
            scores[player] += marble
            other = marbles.move(-7)
            scores[player] += other.item
            marbles = other.move(1)
            other.remove()
        else:
            cur = u.Linked(marble)
            marbles.move(1).add(cur)
            marbles = cur
        player = (player + 1) % players

    return max(scores.values())
    pass


def main():
    ra = a()
    if ra is not None:
        submit(ra, part="a")

    rb = b()
    if rb is not None:
        submit(rb, part="b")


main()
