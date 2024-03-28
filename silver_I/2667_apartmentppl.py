# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque

def apt_count(m, w):
    count = 0

    to_visit = deque()
    to_visit.append((0, 0))
    found = False
    ppl = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while len(to_visit) != 0:
        x, y = to_visit.popleft()
        if m[x][y] == 1:
            if found == False:
                found = True
                count += 1
            else:
                num_ppl += 1
        else:
            if found:
                found = False
                ppl.append(num_ppl)
                num_ppl = 0
        # add neighbors
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and nx < w and ny >= 0 and ny < w:
                to_add = (nx, ny)
                if to_add not in to_visit:
                    to_visit.append((nx, ny))



if __name__ == "__main__":
    n = int(stdin.readline().rstrip())

    _map = []
    for i in range(n):
        lst = []
        num_str = stdin.readline().rstrip()
        for j in range(n):
            lst.append(int(num_str[j]))
        _map.append(lst)

    cnt, ppls = apt_count(_map, n)