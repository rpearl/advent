submit=True
from aocd import data #type: ignore
from aocd import submit as sbmt #type: ignore
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator

data_="""32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

lines = data.splitlines()

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def kind(hand, wildcard):
    counts = Counter(hand)

    if wildcard:
        jcount = counts['J']
        if jcount > 0:
            counts['J'] = 0
            best, _ = counts.most_common(1)[0]
            counts[best] += jcount

    vals = tuple(sorted(c for c in counts.values() if c > 0))

    if vals == (1,1,1,1,1):
        return 1 # high card

    elif vals == (1,1,1,2):
        return 2 # one pair

    elif vals == (1,2,2):
        return 3 # two pair
    elif vals == (1,1,3):
        return 4 # three of a kind
    elif vals == (2,3):
        return 5 # full house
    elif vals == (1,4):
        return 6
    elif vals == (5,):
        return 7
    print(counts)
    raise Exception('no hand?')



def a():
    card_ranks = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    rank_map = {card: len(card_ranks)-i for i, card in enumerate(card_ranks)}

    def sort_key(hand):
        return (kind(hand, wildcard=False),)+tuple(rank_map[card] for card in hand)

    bid_list = [line.split(' ') for line in lines]
    bid_by_hand = {hand: int(bid) for hand, bid in bid_list}
    ranked = sorted(bid_by_hand.keys(), key=sort_key)
    winnings = sum((i+1)*bid_by_hand[hand] for i,hand in enumerate(ranked))
    return winnings
    pass


def b():
    card_ranks = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    rank_map = {card: len(card_ranks)-i for i, card in enumerate(card_ranks)}

    def sort_key(hand):
        return (kind(hand, wildcard=True),)+tuple(rank_map[card] for card in hand)

    bid_list = [line.split(' ') for line in lines]
    bid_by_hand = {hand: int(bid) for hand, bid in bid_list}
    ranked = sorted(bid_by_hand.keys(), key=sort_key)
    winnings = sum((i+1)*bid_by_hand[hand] for i,hand in enumerate(ranked))
    return winnings
    pass

def main():
    submit = globals().get('submit', False)
    astart = time.perf_counter()
    ra = a()
    aend = time.perf_counter()
    if ra is not None:
        print(f"Part a: {ra}")
        print(f"Time taken: {aend-astart:.4f} sec")
        if submit:
            sbmt(ra, part="a")

    bstart = time.perf_counter()
    rb = b()
    bend = time.perf_counter()
    if rb is not None:
        print(f"Part b: {rb}")
        print(f"Time taken: {bend-bstart:.4f} sec")
        if submit:
            sbmt(rb, part="b")
    print()
main()
