import aoc
import intcode
import math
import itertools
from collections import deque, defaultdict
import sys
from sympy.combinatorics.graycode import graycode_subsets

n = len('Command?')
with open('25.in', 'r') as f:
    inp = f.read()

path = ['east\n', 'take sand\n', 'west\n', 'south\n', 'take ornament\n', 'north\n', 'west\n', 'north\n', 'take wreath\n', 'east\n', 'take fixed point\n', 'west\n', 'north\n', 'north\n', 'take spool of cat6\n', 'south\n', 'south\n', 'south\n', 'south\n', 'south\n', 'take candy cane\n', 'north\n', 'east\n', 'south\n', 'north\n', 'east\n', 'east\n', 'take space law space brochure\n', 'south\n', 'take fuel cell\n', 'south\n']

#['east\n', 'take sand\n', 'west\n', 'south\n', 'take ornament\n', 'east\n', 'west\n', 'north\n', 'east\n', 'east\n', 'west\n', 'west\n', 'west\n', 'north\n', 'take wreath\n', 'north\n', 'north\n', 'take spool of cat6\n', 'south\n', 'south\n', 'south\n', 'south\n', 'south\n', 'take candy cane\n', 'north\n', 'east\n', 'east\n', 'east\n', 'take space law space brochure\n', 'west\n', 'south\n', 'north\n', 'west\n', 'west\n', 'east\n', 'east\n', 'east\n', 'south\n', 'take fuel cell\n', 'south\n']
items = [
    'space law space brochure',
    'candy cane',
    'sand',
    'ornament',
    'fuel cell',
    'spool of cat6',
    'wreath',
    'fixed point',
]

def part1():
    all_commands = []
    p = []
    vm = intcode.run(inp, p)

    def add_command(cmd):
        p.extend([ord(c) for c in cmd])
        if cmd[-1] != '\n':
            p.append(ord('\n'))
    for cmd in path:
        add_command(cmd)


    def take(item):
        add_command(f'take {item}')

    def drop(item):
        add_command(f'drop {item}')

    for item in items:
        drop(item)

    def run_until_command(show=False):
        lastn = []
        bad = False
        outp = []
        for c in vm:
            cr = chr(c)
            outp.append(cr)

            if len(lastn) == n:
                lastn.pop(0)
            lastn.append(chr(c))

            s = ''.join(lastn)
            if s == ' heavier' or s == ' lighter':
                bad = True
            if s == 'Command?' and len(p) == 0:
                break
        if not bad and show:
            print(''.join(outp), end='')
        return bad

    run_until_command()

    cur_set = set()

    for subset in graycode_subsets(items):
        if not subset:
            continue
        #print(subset)
        diff = cur_set.symmetric_difference(subset)
        for item in diff:
            if item in cur_set:
                drop(item)
            else:
                take(item)
        cur_set = set(subset)
        run_until_command()
        add_command('west')
        bad = run_until_command(show=True)
        if not bad:
            break

def part2():
    pass

part1()
