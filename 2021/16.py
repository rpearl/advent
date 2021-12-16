submit=True
from aocd import data, lines #type: ignore
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator
from bitstring import BitArray

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]
#data = "D2FE28"
#data="8A004A801A8002F478"
#data="620080001611562C8802118E34"
#data = "D8005AC2A8F0"


def parse_data():
    b = BitArray(hex=data)
    #b = bits(int(data, 16))
    #b = b.rjust(4*len(data), '0')
    ptr = 0
    packets = []
    def read(ln):
        nonlocal ptr
        ret = b[ptr:ptr+ln]
        ptr += ln
        return ret
    def read_packet():
        nonlocal ptr
        ver = read(3).uint
        typ = read(3).uint
        if typ == 4:
            done = False
            val = BitArray()
            while not done:
                group = read(5)
                val.append(group[1:])
                done = group[0] == 0
            return (ver, typ, val.uint)
        else:
            length_id = read(1).uint
            val = []
            if length_id == 0:
                packet_bits = read(15).uint
                start_bit = ptr
                end_bit = packet_bits+start_bit-1
                while ptr < end_bit:
                    val.append(read_packet())
            else:
                num_packets = read(11).uint
                for _ in range(num_packets):
                    val.append(read_packet())
            return (ver, typ, val)
    return read_packet()

tree = parse_data()

def a():
    def add_versions(node):
        ver, typ, val = node
        if typ == 4:
            return ver
        else:
            return ver + sum(add_versions(v) for v in val)
    return add_versions(tree)


def b():
    def evaluate(node):
        ver, typ, children = node
        if typ == 4:
            return children
        else:
            cvals = [evaluate(c) for c in children]
        if typ == 0:
            return sum(cvals)
        elif typ == 1:
            return math.prod(cvals)
        elif typ == 2:
            return min(cvals)
        elif typ == 3:
            return max(cvals)
        elif typ == 5:
            return int(cvals[0] > cvals[1])
        elif typ == 6:
            return int(cvals[0] < cvals[1])
        elif typ == 7:
            return int(cvals[0] == cvals[1])
    return evaluate(tree)

u.main(a, b, submit=globals().get('submit', False))
