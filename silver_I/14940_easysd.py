# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque

def find_cost(m, res, s, r, c):
    to_visit = deque()
    to_visit.append(s)
    res[s[0]][s[1]] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while len(to_visit) != 0:
        x, y = to_visit.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and nx < r and ny >= 0 and ny < c:
                if res[nx][ny] == -1:
                    if m[x][y] > 0 and m[nx][ny] != 0:
                        res[nx][ny] = res[x][y] + 1
                        to_visit.append((nx, ny))

    return res


if __name__ == "__main__":
    row, col = map(int, stdin.readline().split())

    _map = []
    res_map = []
    pos = (-1, -1)
    for i in range(row):
        to_append = list(map(int, stdin.readline().split()))
        res_to_append = [-1 for k in range(col)]
        if 2 in to_append:
            s_c = to_append.index(2)
            pos = (i, s_c)
            res_to_append[s_c] = 0
        if 0 in to_append:
            for j in range(col):
                if to_append[j] == 0:
                    res_to_append[j] = 0
        res_map.append(res_to_append)
        _map.append(to_append)
    res_map = find_cost(_map, res_map, pos, row, col)

    for elem in res_map:
        print(" ".join(map(str, elem)))