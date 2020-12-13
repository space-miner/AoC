def p1(data):
    m = len(data)
    n = len(data[0])
    d = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]
    while True:
        res = []
        for y in range(m):
            row = ''
            for x in range(n):
                s = 0
                for (dx, dy) in d:
                    xx = x + dx
                    yy = y + dy
                    if 0 <= yy < m and 0 <= xx < n:
                        if data[yy][xx] == '#':
                            s += 1
                status = data[y][x]
                if status == '.':
                    row += status
                elif (status == 'L' and s == 0) or (status == '#' and s < 4):
                    row += '#'
                else:
                    row += 'L'
            res.append(row)
        if res == data:
            return sum([row.count('#') for row in res])
        else:
            data = res


def p2(data):
    m = len(data)
    n = len(data[0])
    d = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]
    while True:
        res = []
        for y in range(m):
            row = ''
            for x in range(n):
                s = 0
                for (dx, dy) in d:
                    xx = x + dx
                    yy = y + dy
                    while 0 <= yy < m and 0 <= xx < n and data[yy][xx] in '.':
                        xx += dx
                        yy += dy
                    if 0 <= yy < m and 0 <= xx < n and data[yy][xx] == '#':
                        s += 1
                status = data[y][x]
                if status == '.':
                    row += status
                elif (status == 'L' and s == 0) or (status == '#' and s < 5):
                    row += '#'
                else:
                    row += 'L'
            res.append(row)
        if res == data:
            return sum([row.count('#') for row in res])
        else:
            data = res


input = open('input.txt').read().rstrip()
data = input.split('\n')
print(f'part 1: {p1(data)}')
print(f'part 2: {p2(data)}')
