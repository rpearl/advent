# submit=True
from aocd import lines
import u


def a():
    s = 0
    for line in lines:
        policy, pwd = line.split(":")
        rng, c = policy.split(" ")
        lo, hi = [int(x) for x in rng.split("-")]

        count = len([x for x in pwd if x == c])
        if lo <= count <= hi:
            s += 1
    return s


def b():
    s = 0
    for line in lines:
        policy, pwd = line.split(":")
        pwd = pwd.strip()
        rng, c = policy.split(" ")
        lo, hi = [int(x) for x in rng.split("-")]

        if (pwd[lo - 1] == c) ^ (pwd[hi - 1] == c):
            s += 1
    return s


u.main(a, b, submit=globals().get("submit", False))
