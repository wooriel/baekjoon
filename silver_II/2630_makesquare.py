# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque
from collections import defaultdict

def check(lst_2d:dict, elem:tuple):
    count = 0
    flag = lst_2d[(elem[0], elem[1])]
    for i in range(elem[0], elem[0]+elem[2]):
        for j in range(elem[1], elem[1]+elem[2]):
            if lst_2d[(i, j)] == flag:
                count += 1

    if count == pow(elem[2], 2):
        return flag
    else:
        return -1

if __name__ == "__main__":
    w = int(input())

    color = defaultdict(int)
    for i in range(w):
        lst = list(map(int, stdin.readline().split()))
        for j in range(w):
            if lst[j] == 1:
                color[(i, j)] = 1
# else:
            #     color[(i, j)] = 0

    white = 0
    blue = 0
    nodes = deque()
    # start of row, start of column, width
    cur = (0, 0, w)
    while cur[2] // 2 != 0:
        cur_w = cur[2] // 2
        if cur_w == 1:
            for i in range(cur[0], cur[0]+2):
                for j in range(cur[1], cur[1]+2):
                    if color[(i, j)] == 1:
                        blue += 1
                    else:
                        white += 1
        else:
            neighbors = [(cur[0], cur[1], cur_w),
                        (cur[0], cur[1]+cur_w, cur_w),
                        (cur[0]+cur_w, cur[1], cur_w),
                        (cur[0]+cur_w, cur[1]+cur_w, cur_w)]

            for elem in neighbors:
                # check one color
                # part = color[elem[0]:elem[0]+elem[2], elem[1]:elem[1]+elem[2]]
                f_check = check(color, elem)
                if f_check != -1:
                    if f_check == 0:
                        white += 1
                    else:
                        blue += 1
                else:
                    nodes.append(elem)

        if len(nodes) == 0:
            break
        else:
            cur = nodes.popleft()

    if cur[2] == w: # all tiles are one color
        all_blue = blue // 4 == 1
        all_white = white // 4 == 1
        if all_blue:
            blue = 1
        elif all_white:
            white = 1
        else:
            pass

    print(white)
    print(blue)