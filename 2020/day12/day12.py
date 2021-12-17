def p1(data):
    d = 1
    pos = 0j
    mp = {'N':1j, 'E':1, 'S':-1j, 'W':-1}
    mq = {'R':-1j, 'L':1j} 
    for (op, n) in data:
        if op in mp:
            pos += n * mp[op]
        elif op in mq:
            d *= mq[op] ** (n/90)
        elif op == 'F':
            pos += n * d
    return int(abs(pos.real)+abs(pos.imag))


def p2(data):
    wp = 10+1j
    sp = 0j
    mp = {'N':1j, 'E':1, 'S':-1j, 'W':-1}
    mq = {'R':-1j, 'L':1j}
    for (op, n) in data:
        if op in mp:
            wp += n * mp[op]
        elif op in mq:
            wp *= mq[op] ** (n/90)
        elif op == 'F':
            sp += n * wp
    return int(abs(sp.real)+abs(sp.imag))


input = open('input.txt').read().rstrip()
data = [(line[0], int(line[1:])) for line in input.split('\n')]
print(f'part 1: {p1(data)}')
print(f'part 2: {p2(data)}')
