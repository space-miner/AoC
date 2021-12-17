import collections


def p1(data, k=2020):
    d = collections.defaultdict(lambda : collections.deque([]))
    for i, n in enumerate(data):
        d[n].append(i)
        last = n
    for i in range(len(data), k):
        if len(d[last]) <= 1:
            last = 0
        elif len(d[last]) > 1:
            while len(d[last]) > 2:
                d[last].popleft()
            a, b = d[last]
            last = b - a
        d[last].append(i)
    return last


def p2(data):
    return p1(data, 30000000)


input = open('input.txt').read().rstrip()
data = [int(x) for x in input.split(',')]
print(f'part 1: {p1(data)}')
print(f'part 2: {p2(data)}')