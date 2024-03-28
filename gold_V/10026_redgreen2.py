# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque
from collections import defaultdict

if __name__ == "__main__":
    num = int(stdin.readline())

    color_map = []
    rb_map = []
    for i in range(num):
        mstr = stdin.readline().rstrip()
        mlst = []
        rblst = []
        for i in range(num):
            mlst.append(mstr[i])
            if mstr[i] == 'G':
                rblst.append('R')
            else:
                rblst.append(mstr[i])
        color_map.append(mlst)
        rb_map.append(rblst)

    total, total2 = 0, 0
    # total = 0
    for i in range(num):
        for j in range(num):
            val = color_map[i][j]
            if val != '1':
                x, y = i, j
                neighbor = deque()
                neighbor.append((x, y))
                dx = [1, 0, -1, 0]
                dy = [0, 1, 0, -1]
                # start dfs
                while len(neighbor) != 0:
                    x, y = neighbor.popleft()
                    if color_map[x][y] == '1':
                        continue
                    else:
                        color_map[x][y] = '1'

                        for k in range(4):
                            nx, ny = x + dx[k], y + dy[k]
                            if nx >= 0 and ny >= 0 and nx < num and ny < num:
                                if color_map[nx][ny] == val:
                                    neighbor.append((nx, ny))

                total += 1

            val2 = rb_map[i][j]
            if val2 != '1':
                x, y = i, j
                neighbor = deque()
                neighbor.append((x, y))
                dx = [1, 0, -1, 0]
                dy = [0, 1, 0, -1]
                # start dfs
                while len(neighbor) != 0:
                    x, y = neighbor.popleft()
                    if rb_map[x][y] == '1':
                        continue
                    else:
                        rb_map[x][y] = '1'

                        for k in range(4):
                            nx, ny = x + dx[k], y + dy[k]
                            if nx >= 0 and ny >= 0 and nx < num and ny < num:
                                if rb_map[nx][ny] == val2:
                                    neighbor.append((nx, ny))

                total2 += 1

    print("{} {}".format(total, total2))
    # print(total)
