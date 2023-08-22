# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict

if __name__ == "__main__":
    n = int(stdin.readline())

    E = 0.0000001
    redgenum = round(n*0.15 + E)
    d = defaultdict(int)
    for i in range(n):
        inp = int(stdin.readline())
        d[inp] += 1

    slim = redgenum
    elim = n - redgenum
    count = 0
    sum = 0
    for j in range(1, 30+1):
        for k in range(d[j]):
            if slim <= count and elim > count:
                sum += j
            count += 1

    div = n-2*redgenum
    if sum == 0:
        print(0)
    else:
        avg = round(sum/div + E)
        print(avg)