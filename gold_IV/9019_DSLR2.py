# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque

def get_path(start, e):
    order = deque()
    visited = set()

    visited.add(start)
    order.append((start, ''))
    while True:
        level = []
        while True:
            num_tup = ()
            try:
                num_tup = order.pop()
            except IndexError:
                break
            num = num_tup[0]
            r = (num % 10) * 1000 + (num // 10)
            if r == e:
                return num_tup[1] + 'R'
            if r not in visited:
                level.append((r, num_tup[1] + 'R'))

            l = (num % 1000) * 10 + num // 1000
            if l == e:
                return num_tup[1] + 'L'
            if l not in visited:
                level.append((l, num_tup[1] + 'L'))

            s = 9999 if num == 0 else num - 1
            if s == e:
                return num_tup[1] + 'S'
            if s not in visited:
                level.append((s, num_tup[1] + 'S'))

            d = num * 2 % 10000
            if d == e:
                return num_tup[1] + 'D'
            if d not in visited:
                level.append((d, num_tup[1] + 'D'))
        # extend order
        order.extend(level)
        # update visited
        for elem in level:
            visited.add(elem)
        
        # if d not in visited:
        #     dslr(d, visited)
        # if s not in visited:
        #     dslr(s, visited)
        # if l not in visited:
        #     dslr(l, visited)
        # if r not in visited:
        #     dslr(r, visited)

        # # update visited
        # visited.add(d)

        # path = 'D' + dslr(d, visited)
        # path = 'S' + dslr(s, visited)
        # path = 'L' + dslr(l, visited)
        # path = 'R' + dslr(r, visited)

if __name__ == "__main__":
    n_inp = int(stdin.readline())

    res = []

    for i in range(n_inp):
        start, end = map(int, stdin.readline().split())
        p = get_path(start, end)
        res.append(p)

    for elem in res:
        print(elem)
