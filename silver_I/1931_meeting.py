# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    num_meet = int(input())

    lst = []
    for i in range(num_meet):
        s, e = map(int, stdin.readline().split())
        lst.append([s, e, e-s])

    lst.sort(key=lambda l: l[2])
    lst.sort(key=lambda l: l[1], reverse=True)

    res = []
    cur = lst[0]
    for i in range(1, num_meet):
        cur_s = cur[0]
        next_e = lst[i][1]
        next_s = lst[i][0]
        if next_e <= cur_s:
            res.append(cur)
            cur = lst[i]
        else:
            if next_s > cur_s:
                cur = lst[i]
    if len(res) == 0 or cur[1] <= res[-1][0]:
        res.append(cur)

    print(len(res))