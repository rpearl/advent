# submit=True
from aocd import data, lines
import sys
from collections import Counter, defaultdict, deque, namedtuple
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
from bitsets import bitset
import itertools
import u
import math
import time
import operator

data = """The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant."""
lines = data.splitlines()

chips = []
generators = []
for i, line in enumerate(lines):
    _, items = line.split(" contains ")
    items = items[:-1]
    items = items.replace("-compatible", "")
    if items == "nothing relevant":
        cs = []
        gs = []
    else:
        items = items.replace(" and ", ", ")
        items = [s[2:].replace(",", "").split() for s in items.split(", ")]
        cs = [item for item, typ in items if typ == "microchip"]
        gs = [item for item, typ in items if typ == "generator"]
    chips.append(cs)
    generators.append(gs)
print(chips)
print(generators)
ItemSet = bitset(
    "ItemSet", tuple(itertools.chain.from_iterable(chips)), tuple=True, list=True
)
nfloors = len(chips)

State = namedtuple(
    "State",
    ["cur", "chips", "generators"],
)


def a():
    def combos(state):
        gs = state.generators[state.cur]
        cs = state.chips[state.cur]
        return itertools.chain(
            itertools.product(
                gs.atoms(),
                [ItemSet.infimum],
            ),
            itertools.product(
                (a.union(b) for a, b in itertools.combinations(gs.atoms(), 2)),
                [ItemSet.infimum],
            ),
            itertools.product(gs.atoms(), cs.atoms()),
            itertools.product(
                [ItemSet.infimum],
                cs.atoms(),
            ),
            itertools.product(
                [ItemSet.infimum],
                (a.union(b) for a, b in itertools.combinations(cs.atoms(), 2)),
            ),
        )

    def compatible(generators, chips):
        return not generators or chips.intersection(generators) == chips

    def replace(s, vals):
        l = ItemSet.List.fromints(s)
        for i, v in vals:
            l[i] = v
        return ItemSet.Tuple.fromints(l)

    def move_to_floor(state, floor, combo):
        ngs = state.generators[floor].union(combo[0])
        ncs = state.chips[floor].union(combo[1])
        if not compatible(ngs, ncs):
            return None

        ngenerators = replace(
            state.generators,
            [
                (state.cur, state.generators[state.cur].difference(combo[0])),
                (floor, ngs),
            ],
        )
        nchips = replace(
            state.chips,
            [
                (state.cur, state.chips[state.cur].difference(combo[1])),
                (floor, ncs),
            ],
        )
        return State(cur=floor, chips=nchips, generators=ngenerators)

    def adjacent(state):
        for combo in combos(state):
            if state.cur > 0:
                nstate = move_to_floor(state, state.cur - 1, combo)
                if nstate is not None:
                    yield nstate
            if state.cur < nfloors - 1:
                nstate = move_to_floor(state, state.cur + 1, combo)
                if nstate is not None:
                    yield nstate

    def canonicalized(state):
        floor_for_gen = {}
        floor_for_chip = {}
        for floor in range(nfloors):
            for g in state.generators[floor]:
                floor_for_gen[g] = floor
            for c in state.chips[floor]:
                floor_for_chip[c] = floor
        pairs = tuple(
            sorted((floor_for_gen[it], floor_for_chip[it]) for it in ItemSet.supremum)
        )
        return pairs

    target_items = ItemSet.Tuple.fromints(
        ([ItemSet.infimum] * (nfloors - 1)) + [ItemSet.supremum]
    )
    target = State(cur=nfloors - 1, chips=target_items, generators=target_items)

    initial = State(
        cur=0,
        generators=ItemSet.Tuple.frommembers(generators),
        chips=ItemSet.Tuple.frommembers(chips),
    )

    dist = {}
    pred = {}
    seen = set()
    dist[initial] = 0
    queue = deque([(initial, None)])
    print(".")
    while queue:
        node, parent = queue.popleft()
        pred[node] = parent
        if parent:
            dist[node] = dist.get(parent, 0) + 1
        if node == target:
            print("got here")
            break
        seen.add(canonicalized(node))
        for child in adjacent(node):
            if canonicalized(child) in seen:
                continue
            queue.append((child, node))
    # print(dist)
    return dist[target]


def b():
    pass


u.main(a, b, submit=globals().get("submit", False))
