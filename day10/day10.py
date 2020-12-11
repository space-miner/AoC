import collections


def p1(data):
    data.sort()
    data = [0] + data + [max(data)+3]
    d = {1:0, 2:0, 3:0}
    z = zip(data[:-1], data[1:])
    for (a,b) in z:
        d[b-a] += 1
    return d[3]*d[1]


def p2(data):
    data.sort()
    d = collections.defaultdict(int)
    d[0] = 1
    for n in data:
        for i in range(1,4):
            if n-i >= 0:
                d[n] += d[n-i]
    return d[max(data)]


input = open('input.txt').read().rstrip()
data = [int(num) for num in input.split('\n')]
print(f'part 1: {p1(data)}')
print(f'part 2: {p2(data)}')
