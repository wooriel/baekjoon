# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict
from collections import deque

if __name__ == "__main__":
    c, r = map(int, stdin.readline().split())

    nodes = deque()
    visited = set()
    box = defaultdict(int)
    num_zero = 0
    for i in range(r):
        col = list(map(int, stdin.readline().split()))
        for j in range(c):
            if col[j] != 0:
                if col[j] == 1:
                    nodes.append((i, j, 0))
                    visited.add((i, j))
                box[(i, j)] = col[j]
            else:
                num_zero += 1
        
    
    while len(nodes) != 0:
        cur = nodes.popleft()

        neighbors = [(cur[0], cur[1] + 1),
                     (cur[0] + 1, cur[1]),
                     (cur[0], cur[1] - 1),
                     (cur[0] - 1, cur[1])]
        
        for elem in neighbors:
            if elem[0] >= 0 and elem[0] < r and elem[1] >= 0 and elem[1] < c:
                if box[elem] == 0 and elem not in visited:
                    box[elem] = 1
                    num_zero -= 1
                    nodes.append((elem[0], elem[1], cur[2] + 1))
                    visited.add(elem)

    if num_zero == 0:
        print(cur[2])
    else:
        print(-1)