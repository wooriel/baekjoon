# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque
from collections import defaultdict

if __name__ == "__main__":
    num = int(stdin.readline())

    color_map = []
    for i in range(num):
        mstr = stdin.readline().rstrip()
        color_map.append(mstr)

    gp_color = deque()
    visited = set()
    x, y = 0, 0
    scolor = color_map[x][y]
    gp_color.append((scolor, x, y))
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    ans = defaultdict(int)
    ans2 = defaultdict(int)
    ans[scolor] += 1
    ans2[scolor] += 1
    while len(gp_color) > 0:
        col, x, y = gp_color.popleft()
        if (x, y) in visited:
            continue
        else:
            visited.add((x, y))

            for i in range(2):
                nx, ny = x + dx[i], y + dy[i]
                if nx >= 0 and ny >= 0 and nx < num and ny < num:
                    ncolor = color_map[nx][ny]
                    gp_color.append((ncolor, nx, ny))
                    if col != ncolor:
                        ans[ncolor] += 1
                        # no difference between 'R' and 'G'
                        if col == 'B' or ncolor == 'B':
                            ans2[ncolor] += 1
                            
            for i in range(2, 4):
                px, py = x + dx[i], y + dx[i]
                ppx, ppy = x-1, y-1
                if px >= 0 and py >= 0 and ppx >= 0 and ppy >= 0:
                    pcolor = color_map[px][py]
                    ppcolor = color_map[ppx][ppy]
                    if pcolor == col and ppcolor != col:
                        ans[col] -= 1
                        if pcolor == 'B':
                            ans2[col] -= 1
                    if ppcolor == 'B' and pcolor != 'B' and col != 'B':
                        ans2[col] -= 1
                    else:
                        continue                    
                        

    total = 0
    val = list(ans.values())
    for elem in val:
        total += elem

    total2 = 0
    val2 = list(ans2.values())
    for elem in val2:
        total2 += elem

    print("{} {}".format(total, total2))
