import string
import sys
from collections import deque,defaultdict
import math
import heapq
import itertools
from sympy.combinatorics.permutations import Permutation, Cycle
inp = sys.stdin.readlines()

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m

def parse_insns(inp):
    insns = []
    for insn in inp:
        if insn.startswith('deal into'):
            insns.append(('rev', None))
        elif insn.startswith('deal with increment'):
            n = int(insn.split(' ')[-1])
            insns.append(('inc', n))
        elif insn.startswith('cut '):
            n = int(insn.split(' ')[1])
            insns.append(('cut', n))
    return insns

def part1():
    #D = 10007
    D = 10
    insns = parse_insns(inp)
    xs = list(range(10))
    for op, n in insns:
        nxs = []
        for x in xs:
            if op == 'rev':
                x = D - 1 - x
            elif op == 'cut':
                x = (x+n+D) % D
            elif op == 'inc':
                x = (x * n) % D
            nxs.append(x)
        xs = nxs
    print(xs)
    #return x

print(part1())
