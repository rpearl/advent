import sys
import aoc
import intcode
from collections import defaultdict

inp = sys.stdin.read()
class BufferList:
    def __init__(self, addr, idle):
        self.addr = addr
        self.l = [addr]
        self.idle = idle
    def pop(self, _):
        if self.l:
            self.idle[self.addr] = False
            return self.l.pop(0)
        else:
            self.idle[self.addr] = True
            return -1
    def append(self, val):
        self.l.append(val)
    def __len__(self):
        return len(self.l)

def part1():
    idle = [False]*50
    buffers = [BufferList(i, idle) for i in range(50)]

    outputs = defaultdict(list)

    vms = [intcode.run(inp, buffers[addr], yield_steps=True) for addr in range(50)]

    while True:
        for addr, vm in enumerate(vms):
            o = next(vm)
            if o == 'step':
                continue
            outputs[addr].append(o)
            if len(outputs[addr]) == 3:
                a, x, y = outputs[addr]
                outputs[addr] = []
                if a == 255:
                    return y
                buffers[a].append(x)
                buffers[a].append(y)

def part2():
    idle = [False]*50
    buffers = [BufferList(i, idle) for i in range(50)]


    nat = None
    last_naty = None

    outputs = defaultdict(list)
    def cpu(addr):
        def set_idle(val):
            idle[addr] = val
        return intcode(inp, buffers[addr], set_idle=set_idle)

    vms = [intcode.run(inp, buffers[addr], yield_steps=True) for addr in range(50)]
    def is_idle():
        return nat and all(idle) and all(len(buffer) == 0 for buffer in buffers)
    while True:
        for addr, vm in enumerate(vms):
            o = next(vm)
            if o == 'step':
                continue
            outputs[addr].append(o)
            if len(outputs[addr]) == 3:
                a, x, y = outputs[addr]
                outputs[addr] = []
                if a == 255:
                    nat = (x,y)
                else:
                    buffers[a].append(x)
                    buffers[a].append(y)
        if is_idle():
            natx, naty = nat
            buffers[0].append(natx)
            buffers[0].append(naty)
            if naty == last_naty:
                return naty
            last_naty = naty

print(part1())
print(part2())
