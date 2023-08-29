# -*- coding: utf-8 -*-
from sys import stdin
import math
from functools import reduce

def cal_level(lst):
    newlst = []
    lst.sort()
    for i in range(n // 2 + 1):
        newlst.append(lst[i] + lst[len(lst) - i - 1])
    return newlst

def cal_cost(n, lst):
    lstsum = reduce(lambda x, y: x + y, lst)
    sum = 0
    while n // 2 > 1:
        if n % 2 == 0:
            sum += lstsum
        else:
            sum = sum + lstsum - max(lst)
        # create lst
        cal_level()

if __name__ == "__main__":
    n = int(stdin.readline())

    for i in range(n):
        m = int(stdin.readline())
        file = list(map(int, stdin.readline().split()))
        newlst = cal_level(file)
