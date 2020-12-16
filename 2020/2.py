from aocd import data, submit
import sys

print(len(data.split("\n")))

if len(sys.argv) < 2 or sys.argv[1] != "y":
    submit = lambda *k, **a: None


def a():
    s = 0
    for line in data.split("\n"):
        policy, pwd = line.split(":")
        rng, c = policy.split(" ")
        lo, hi = [int(x) for x in rng.split("-")]

        count = len([x for x in pwd if x == c])
        if lo <= count <= hi:
            s += 1
    return s


def b():
    s = 0
    for line in data.split("\n"):
        policy, pwd = line.split(":")
        pwd = pwd.strip()
        rng, c = policy.split(" ")
        lo, hi = [int(x) for x in rng.split("-")]

        if (pwd[lo - 1] == c) ^ (pwd[hi - 1] == c):
            s += 1
    return s


def main():
    ra = a()
    if ra:
        print(ra)
        submit(ra, part="a")

    rb = b()
    if rb:
        print(rb)
        submit(rb, part="b")


main()
