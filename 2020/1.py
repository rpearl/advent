from aocd import data, submit
import u
import itertools

items = set(u.ints(data))


def a():
    for x in items:
        y = 2020 - x
        if y in items:
            return x * y


def b():
    for x, y in itertools.combinations(items, 2):
            z = 2020 - x - y
            if z in items:
                return x * y * z


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
