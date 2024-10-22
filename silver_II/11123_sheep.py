# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque

if __name__ == "__main__":
    cases = int(stdin.readline())
    idx = []
    for i in range(cases):
        r, c = map(int, stdin.readline().split())
        # _grid = []
        for i in range(r):
            lst = []
            line = stdin.readline().rstrip()
            for j in range(c):
                cur = line[j]
                # lst.append(cur)
                if cur == '#':
                    idx.append((i, j))
            # _grid.append(lst)

        dr = [-1, 0, 1, 0]
        dc = [0, -1, 0, 1]
        visited = set()
        count = 0
        while len(idx) > 0:
            cur = idx.pop()
            count += 1
            # visited.add(cur)
            to_visit = deque()
            to_visit.appendleft(cur)
            while len(to_visit) > 0:
                cr, cc = to_visit.popleft()
                for i in range(4):
                    nr, nc = cr+dr[i], cc+dc[i]
                    if 0 <= nr < r and 0 <= nc < c:
                        cidx = (nr, nc)
                        try:
                            loc = idx.index(cidx)
                            del idx[loc]
                            to_visit.appendleft(cidx)
                            # visited.add(cidx)
                        except ValueError:
                            continue

        print(count)
