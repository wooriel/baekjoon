# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque

def count_f(m, p, row, col):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    to_visit = deque()
    to_visit.append(p)
    visited = set()
    visited.add(p)
    count = 0
    while len(to_visit) != 0:
        cur = to_visit.popleft()
        cur_let = m[cur[0]][cur[1]]
        if cur_let == "P":
            count += 1
        for i in range(4):
            x = cur[0] + dx[i]
            y = cur[1] + dy[i]
            if (x, y) not in visited:
                if x >= 0 and x < row and y >= 0 and y < col:
                    letter = m[x][y]
                    if letter == "O" or letter == "P":
                        to_visit.append((x, y))
                        visited.add((x, y))

    return count

if __name__ == "__main__":
    r, c = map(int, stdin.readline().split())

    map = []
    pos  = (0, 0)
    for i in range(r):
        w = stdin.readline().rstrip()
        if 'I' in w:
            s_c = w.find('I')
            pos = (i, s_c)
        map.append(w)

    c = count_f(map, pos, r, c)
    if c == 0:
        print("TT")
    else:
        print(c)