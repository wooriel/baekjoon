# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque


if __name__ == "__main__":
    n, m = map(int, stdin.readline().split())

    _map = []
    for i in range(n):
        _str = stdin.readline().rstrip()
        _lst = []
        for j in range(m):
            _lst.append(int(_str[j]))
        _map.append(_lst)

    if n == 1 and m == 1:
        print(1)
    else:
        path = deque()
        path.append((0, 0, 1, 1))

        visited0 = set()
        visited0.add((0, 0))
        visited1 = set()
        # visited1.add((0, 0))  # 1이 안되어있어서
        max_cnt = n*m+1
        while len(path) > 0:
            r, c, one, cnt = path.popleft()
            dr = [-1, 0, 1, 0]
            dc = [0, -1, 0, 1]
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if nr == n-1 and nc == m-1 and max_cnt > cnt+1:
                    max_cnt = cnt+1
                elif 0 <= nr < n and 0 <= nc < m:
                    if _map[nr][nc] == 0 and ((nr, nc) not in visited0 or (nr, nc) not in visited1):
                        if one == 1 and (nr, nc) not in visited0:
                            visited0.add((nr, nc))
                            path.append((nr, nc, one, cnt+1))
                        elif one == 0 and (nr, nc) not in visited1:
                            visited1.add((nr, nc))
                            path.append((nr, nc, one, cnt+1))
                    elif _map[nr][nc] == 1 and one == 1 and (nr, nc) not in visited1:
                        path.append((nr, nc, 0, cnt+1))
                        visited1.add((nr, nc))

        if max_cnt == n*m+1:
            print(-1)
        else:
            print(max_cnt)
