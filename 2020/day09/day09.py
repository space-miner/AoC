import collections


def p1(data, k):
    c = collections.Counter(data[:k])
    for i in range(k, len(data)):
        n = data[i]
        m = data[i-k]
        s = set(c.keys())
        if any([(n-e) in s for e in s if e != n-e]+[n % 2 == 0 and n//2 in s and c[n//2] > 1]):
            c[n] += 1
            c[m] -= 1
            if c[m] == 0:
                del c[m]
        else:
            return n
            

def p2(data, tgt):
    d = collections.defaultdict(int)
    s = 0
    for i, n in enumerate(data):
        s += n
        t = s-tgt
        if t in d:
            arr = data[d[t]:i+1]
            return max(arr)+min(arr)
        else:
            d[s] = i+1


input = open('input.txt').read().rstrip()
data = [int(line) for line in input.split('\n')]
print(f'part 1: {p1(data, 25)}')
print(f'part 2: {p2(data, p1(data, 25))}')
