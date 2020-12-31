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


def apply_effects(state):
    player_armor = 0
    if state.shield_effect > 0:
        player_armor += 7
    boss_hp = state.boss_hp
    if state.poison_effect > 0:
        boss_hp -= 3
    player_mana = state.player_mana
    if state.recharge_effect > 0:
        player_mana += 101
    shield_effect = max(state.shield_effect - 1, 0)
    poison_effect = max(state.poison_effect - 1, 0)
    recharge_effect = max(state.recharge_effect - 1, 0)
    return state._replace(
        player_armor=player_armor,
        boss_hp=boss_hp,
        player_mana=player_mana,
        shield_effect=shield_effect,
        poison_effect=poison_effect,
        recharge_effect=recharge_effect,
    )


def apply_cost(state, cost):
    state = apply_effects(state)
    if state.player_mana < cost:
        return None, None
    return (
        state._replace(player_mana=state.player_mana - cost),
        cost,
    )


def magic_missile(state):
    state, cost = apply_cost(state, 53)
    if not state:
        return None, None
    return (
        state._replace(
            boss_hp=state.boss_hp - 4,
        ),
        cost,
    )


def drain(state):
    state, cost = apply_cost(state, 73)
    if not state:
        return None, None
    return (
        state._replace(
            player_hp=state.player_hp + 2,
            boss_hp=state.boss_hp - 2,
        ),
        cost,
    )


def shield(state):
    state, cost = apply_cost(state, 113)
    if not state or state.shield_effect != 0:
        return None, None
    return (
        state._replace(
            shield_effect=6,
        ),
        cost,
    )


def poison(state):
    state, cost = apply_cost(state, 173)
    if not state or state.poison_effect != 0:
        return None, None
    return (
        state._replace(
            poison_effect=6,
        ),
        cost,
    )


def recharge(state):
    state, cost = apply_cost(state, 229)
    if not state or state.recharge_effect != 0:
        return None, None
    return (
        state._replace(
            recharge_effect=5,
        ),
        cost,
    )


def boss_turn(state):
    state = apply_effects(state)
    if state.boss_hp <= 0:
        return state
    damage = max(1, state.boss_dmg - state.player_armor)
    return state._replace(
        player_hp=state.player_hp - damage,
    )


State = namedtuple(
    "State",
    [
        "player_hp",
        "player_armor",
        "player_mana",
        "shield_effect",
        "poison_effect",
        "recharge_effect",
        "boss_hp",
        "boss_dmg",
    ],
)

spells = [
    magic_missile,
    drain,
    shield,
    poison,
    recharge,
]


@functools.cache
def search(state, cur_cost, hard_mode):
    if state.boss_hp <= 0:
        return cur_cost
    if hard_mode:
        state = state._replace(player_hp=state.player_hp - 1)
    if state.player_hp <= 0:
        return math.inf
    best = math.inf
    for spell in spells:
        nstate, cost = spell(state)
        if not nstate:
            continue
        cur = search(boss_turn(nstate), cur_cost + cost, hard_mode)
        if cur < best:
            best = cur
    return best


def a():
    boss_hp, boss_dmg = u.ints(data)
    state = State(
        player_hp=50,
        player_armor=0,
        player_mana=500,
        shield_effect=0,
        poison_effect=0,
        recharge_effect=0,
        boss_hp=boss_hp,
        boss_dmg=boss_dmg,
    )
    return search(state, 0, False)


def b():

    boss_hp, boss_dmg = u.ints(data)
    state = State(
        player_hp=50,
        player_armor=0,
        player_mana=500,
        shield_effect=0,
        poison_effect=0,
        recharge_effect=0,
        boss_hp=boss_hp,
        boss_dmg=boss_dmg,
    )
    return search(state, 0, True)
    pass


u.main(a, b, submit=globals().get("submit", False))
