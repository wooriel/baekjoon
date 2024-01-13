# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque
from collections import defaultdict

if __name__ == "__main__":
    r, c = map(int, stdin.readline().split())

    cur = (0, 0, 1)

    maze = defaultdict(int)
    for i in range(r):
        line = stdin.readline()[:-1]
        for j in range(c):
            if int(line[j]) == 1:
                maze[(i, j)] = 1

    path = deque()
    visited = set()
    while cur[0] != r-1 or cur[1] != c-1:
        r_pos = cur[0]
        c_pos = cur[1]
        step = cur[2]
        neigh = [(cur[0], cur[1] + 1),
                (cur[0] + 1, cur[1]),
                (cur[0] - 1, cur[1]),
                (cur[0], cur[1] - 1)]
        
        for elem in neigh:
            if elem[0] < 0 or elem[1] < 0 or elem[0] >= r or elem[1] >= c:
                continue
            if maze[elem] == 1 and elem not in visited:
                path.append((elem[0], elem[1], cur[2] + 1))
                visited.add((elem[0], elem[1])) # 위치가 중요 안그러면 중복되어 탐색
        cur = path.popleft()

    print(cur[2])
