import copy

def p1(data):
    s = set()
    acc = 0
    i = 0
    while i < len(data):
        op, num = data[i]
        if i not in s:
            s.add(i)
            if op == 'nop':
                i += 1
                continue
            elif op == 'acc':
                acc += int(num)
                i += 1
            elif op == 'jmp':
                i += int(num)
        elif i in s:
            return acc


def loop(data):
    s = set()
    acc = 0
    i = 0
    while i < len(data):
        op, num = data[i]
        if i not in s:
            s.add(i)
            if op == 'nop':
                i += 1
                continue
            elif op == 'acc':
                acc += int(num)
                i += 1
            elif op == 'jmp':
                i += int(num)
        elif i in s:
            return (i >= len(data), acc)
    return True, acc
        

def p2(data):
    acc = 0
    for i, (op, num) in enumerate(data):
        prog = copy.deepcopy(data)
        if op == 'nop':
            prog[i][0] = 'jmp'
        elif op == 'jmp':
            prog[i][0] = 'nop'
        else:
            continue
        halt, acc = loop(prog)
        if halt:
            return acc


input = open('input.txt').read().rstrip()
data = [line.split() for line in input.split('\n')]
print(f'part 1: {p1(data)}')
print(f'part 2: {p2(data)}')

