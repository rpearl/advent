from aocd import lines, submit
import sys
from collections import Counter, defaultdict, deque
import cachetools
import itertools
import u


def nosubmit(answer, part):
    print(f"Part {part}:\n{answer}")


# submit = nosubmit


print(f"File line count: {len(lines)}")


def a():
    log = []
    for line in lines:
        ts, action = line.split("] ")
        ts = ts[1:]
        log.append((ts, action))
    log.sort()
    minutes = defaultdict(Counter)
    active = None
    sleeping = None
    for ts, action in log:
        if "begins shift" in action:
            active = "".join(c for c in action if c.isdigit())
        else:
            assert active is not None
            _, time = ts.split(" ")
            hh, mm = [int(x) for x in time.split(":")]
            m = 60 * hh + mm
            if sleeping is not None:
                assert action == "wakes up"
                for i in range(sleeping, m):
                    minutes[active][i] += 1
                sleeping = None
            else:
                sleeping = m
    most_asleep_minutes = 0
    most_asleep = None
    for guard, count in minutes.items():
        m = sum(count.values())
        if m > most_asleep_minutes:
            most_asleep = guard
            most_asleep_minutes = m

    best_minute = None
    n = -1
    for minute, nn in minutes[most_asleep].items():
        if nn > n:
            best_minute = minute
            n = nn
    return int(most_asleep) * best_minute

    pass


def b():
    log = []
    for line in lines:
        ts, action = line.split("] ")
        ts = ts[1:]
        log.append((ts, action))
    log.sort()
    minutes = defaultdict(Counter)
    active = None
    sleeping = None
    for ts, action in log:
        if "begins shift" in action:
            active = "".join(c for c in action if c.isdigit())
        else:
            assert active is not None
            _, time = ts.split(" ")
            hh, mm = [int(x) for x in time.split(":")]
            m = 60 * hh + mm
            if sleeping is not None:
                assert action == "wakes up"
                for i in range(sleeping, m):
                    minutes[active][i] += 1
                sleeping = None
            else:
                sleeping = m
    max_count = 0
    max_minute = 0
    max_guard = None

    for guard, count in minutes.items():
        print(max_guard, max_minute)
        for m, n in count.items():
            if n > max_count:
                max_minute = m
                max_guard = guard
                max_count = n
    return int(max_guard) * max_minute


def main():
    ra = a()
    if ra is not None:
        submit(ra, part="a")

    rb = b()
    if rb is not None:
        submit(rb, part="b")


main()
