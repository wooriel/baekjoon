# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque

if __name__ == "__main__":
    n = int(stdin.readline())

    _map = []
    _max = -1
    for i in range(n):
        lst = list(map(int, stdin.readline().split()))
        cur_max = max(lst)
        if _max < cur_max:
            _max = cur_max
        _map.append(lst)

    res = []
    for m in range(_max, -1, -1):
        if m == _max:
            res.append(0)
        else:
            count = 0
            next_square = deque()
            visited = set()

            dx = [1, 0, -1, 0]
            dy = [0, 1, 0, -1]
            for i in range(n):
                for j in range(n):
                    if (i, j) not in visited:
                        visited.add((i, j))
                        if _map[i][j] > m:
                            count += 1
                            next_square.append([i, j])
                            while len(next_square) > 0:
                                cx, cy = next_square.popleft()
                                for k in range(4):
                                    nx = cx + dx[k]
                                    ny = cy + dy[k]
                                    if nx >= 0 and nx < n and ny >= 0 and ny < n:
                                        if (nx, ny) not in visited:
                                            if _map[nx][ny] > m:
                                                next_square.append([nx, ny])
                                                visited.add((nx, ny))

            res.append(count)
    print(max(res))