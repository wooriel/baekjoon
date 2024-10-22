# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque
# from collections import defaultdict

if __name__ == "__main__":
    _n, _m = map(int, stdin.readline().split())

    _map = []

    dist = deque()
    visited = set()
    for i in range(_n):
        _lst = list(map(int, stdin.readline().split()))
        for j in range(_m):
            if _lst[j] == 1:
                dist.append((i, j, 0))
                visited.add((i, j))
        _map.append(_lst)

    max_dist = 0
    while len(dist) > 0:
        _i, _j, _d = dist.popleft()
        dr = [-1, -1, -1, 0, 0, 1, 1, 1]
        dc = [-1, 0, 1, -1, 1, -1, 0, 1]
        for i in range(8):
            nr, nc, nd = _i+dr[i], _j+dc[i], _d+1
            if 0 <= nr < _n and 0 <= nc < _m and (nr, nc) not in visited:
                _map[nr][nc] = nd
                visited.add((nr, nc))
                dist.append((nr, nc, nd))
                if max_dist < nd:
                    max_dist = nd
        if len(visited) == _n*_m:
            break

    print(max_dist)
