from aocd import data, submit
import sys

# data = """..##.......
##...#...#..
# .#....#..#.
# ..#.#...#.#
# .#...##..#.
# ..#.##.....
# .#.#.#....#
# .#........#
##.##...#...
##...##....#
# .#..#...#.#"""

print(len(data.split("\n")))

if len(sys.argv) < 2 or sys.argv[1] != "y":
    submit = lambda *k, **a: None


def a():
    grid = data.split("\n")
    s = 0
    x = 0
    y = 0
    while y < len(grid):
        if grid[y][x % len(grid[0])] == "#":
            s += 1
        x += 3
        y += 1
    return s


def b():
    grid = data.split("\n")
    ss = 1
    for dx, dy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        s = 0
        x = 0
        y = 0
        while y < len(grid):
            if grid[y][x % len(grid[0])] == "#":
                s += 1
            x += dx
            y += dy
        ss *= s
    return ss


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
