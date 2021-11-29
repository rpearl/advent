from collections import defaultdict

def run(program, program_input=None, yield_steps=False):
    ip = rb = 0
    if isinstance(program, str):
        program = map(int, program.split(','))
    if not isinstance(program, defaultdict):
        mem = defaultdict(int, enumerate(program))
    else:
        mem = program

    while True:
        om = mem[ip]
        modev, op = divmod(om, 100)
        if op == 99:
            return
        oldip = ip
        def read(i):
            mode = (modev // (10**i)) % 10
            x = mem[oldip+i+1]
            if mode == 0: return mem[x]
            if mode == 1: return x
            if mode == 2: return mem[x+rb]

        def write(i, v):
            mode = (modev // (10**i)) % 10
            x = mem[oldip+i+1]
            if mode == 0: mem[x]=v
            elif mode == 2: mem[x+rb]=v
            else: raise Exception('??')

        #ip += size
        if op == 1:
            ip += 4
            write(2, read(0) + read(1))
        elif op == 2:
            ip += 4
            write(2, read(0) * read(1))
        elif op == 3:
            ip += 2
            write(0, program_input.pop(0))
        elif op == 4:
            ip += 2
            yield read(0)
        elif op == 5:
            if read(0):
                ip = read(1)
            else:
                ip += 3
        elif op == 6:
            if not read(0):
                ip = read(1)
            else:
                ip += 3
        elif op == 7:
            ip += 4
            write(2, int(read(0) < read(1)))
        elif op == 8:
            ip += 4
            write(2, int(read(0) == read(1)))
        elif op == 9:
            ip += 2
            rb += read(0)
        if yield_steps:
            yield 'step'

def disassemble(program):
    sizes = dict(enumerate([1, 4, 4, 2, 2, 3, 3, 4, 4, 2]))
    names = {
        1: 'ADD', 2: 'MUL', 3: 'IN', 4: 'OUT',
        5: 'JNZ', 6: 'JZ', 7: 'LT', 8: 'EQ',
        9: 'RB', 99: 'HALT',
    }
    if isinstance(program, str):
        program = list(map(int, program.split(',')))
    i = 0
    while i < len(program):
        op = program[i] % 100
        size = sizes.get(op, 1)
        name = names.get(op, '?')
        args = [program[i + j] for j in range(1, size)]
        modes = [(program[i] // 10 ** j) % 10 for j in range(2, 5)]
        tokens = [name]
        for arg, mode in zip(args, modes):
            if mode == 0:
                tokens.append('%d' % arg)
            elif mode == 1:
                tokens.append('#%d' % arg)
            elif mode == 2:
                tokens.append('[%d]' % arg)
        print('%04d' % i, '%6d' % program[i], ' '.join(tokens))
        i += size

if __name__ == '__main__':
    import fileinput
    disassemble(list(fileinput.input())[0])
