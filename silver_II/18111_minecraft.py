# -*- coding: utf-8 -*-
from sys import stdin
from functools import reduce
import math

# def cal_cost(orig, bnum):
#     # returns cost and blocks used
#     # if bnum == orig:
#     #     return 0, 0
#     if bnum > orig:
#         return 2*(bnum-orig), orig-bnum # minus
#     else: # bnum < orig
#         return orig-bnum, orig-bnum # plus

if __name__ == "__main__":
    h, w, blocks = map(int, stdin.readline().split())

    # remove - 2sec, add - 1sec

    lst = []
    # sum = 0
    bmin, bmax = 501, 0
    for i in range(h):
        lst.append(list(map(int, stdin.readline().split())))
        # sum += reduce(lambda x, y: x + y, lst[i])
        curmax = max(lst[i])
        curmin = min(lst[i])
        if curmax > bmax:
            bmax = curmax
        if curmin < bmin:
            bmin = curmin

    min_cost = bmax * h * w * 2
    t = 0

    for k in range(bmin, bmax+1):
        total_cost = 0
        r = blocks
        for i in range(h):
            for j in range(w):
                # tup = cal_cost(k, lst[i][j])
                cost = k - lst[i][j]
                if cost >= 0:
                    total_cost += cost
                else:
                    total_cost += -2 * cost
                r -= cost
                # total_cost += tup[0]
                # r -= tup[1]

        if r >= 0 and total_cost <= min_cost:
            min_cost = total_cost
            t = k

    print("{} {}".format(min_cost, t))