# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque

def bfs(s, e):
    if s == e:
        return ''
    lst = deque()
    lst.append((s, ''))
    visited = set()
    visited.add(s)

    while len(lst) > 0:
        cur = lst.popleft()
        strnum = cur[0]
        path = cur[1]
        d = str(int(strnum) * 2 % 10000).zfill(4)
        s = int(strnum) - 1
        if s < 0:
            s = 9999
        s = str(s).zfill(4)
        l = strnum[1:] + strnum[0]
        r = strnum[3] + strnum[0:3]
        p_d = path + 'D'
        p_s = path + 'S'
        p_l = path + 'L'
        p_r = path + 'R'
        if d == e:
            return p_d
        elif d not in visited:
            lst.append((d, p_d))
            visited.add(d)
        if s == e:
            return p_s
        elif s not in visited:
            lst.append((s, p_s))
            visited.add(s)
        if l == e:
            return p_l
        elif l not in visited:
            lst.append((l, p_l))
            visited.add(l)
        if r == e:
            return p_r
        elif r not in visited:
            lst.append((r, p_r))
            visited.add(r)
    return 'not working'
        

if __name__ == "__main__":
    cases = int(stdin.readline().rstrip())

    for i in range(cases):
        start, end = stdin.readline().split()
        start = start.zfill(4)
        end = end.zfill(4)
        p = bfs(start, end)
        print(p)