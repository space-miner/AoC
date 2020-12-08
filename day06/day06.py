import collections


def p1(data):
    res = 0
    for grp in data:
        s = set(''.join(grp.split('\n')))
        res += len(s)
    return res


def p2(data):
    res = 0
    for grp in data:
        s = set('abcdefghijklmnopqrstuvwxyz')
        for ans in grp.split('\n'):
            s &= set(ans)
        res += len(s)
    return res


input = open('input.txt').read().rstrip()
data = input.split('\n\n')
print(f'part 1: {p1(data)}')
print(f'part 2: {p2(data)}')
