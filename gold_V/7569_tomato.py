# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque


if __name__ == "__main__":
    col, row, height = map(int, stdin.readline().split())
    total = col * row * height
    red_toma = deque()
    tomato = []
    for i in range(height):
        box = []
        for j in range(row):
            one_c = list(map(int, stdin.readline().split()))
            for k in range(col):
                if one_c[k] == 1:
                    red_toma.append((i, j, k, 0))
                elif one_c[k] == -1:
                    total -= 1
            box.append(one_c)
        tomato.append(box)

    # 3D array
    dh = [0, 0, 0, 0, -1, 1] # z-dir
    dr = [0, 0, -1, 1, 0, 0] # y-dir
    dc = [-1, 1, 0, 0, 0, 0] # x-dir
    max_cnt = 0
    while len(red_toma) > 0:
        h, r, c, cnt = red_toma.popleft()
        if max_cnt < cnt:
            max_cnt = cnt
        ncnt = cnt + 1
        # 1인 부분이므로 total에서 빼주면 됨
        total -= 1

        # add neighbors
        for i in range(6):
            nh, nr, nc = h+dh[i], r+dr[i], c+dc[i]
            if nh >= 0 and nh < height and nr >= 0 and nr < row and nc >= 0 and nc < col:
                if tomato[nh][nr][nc] == 0:
                    # change into 1
                    tomato[nh][nr][nc] = 1
                    red_toma.append((nh, nr, nc, ncnt))
                # -1이랑 1일때는 무시
                
        if total == 0:
            break

    if total == 0:
        print(max_cnt)
    else:
        print(-1)