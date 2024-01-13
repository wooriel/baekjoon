# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    n = int(stdin.readline().rstrip())

    res = []
    for i in range(n):
        lst = list(map(int, stdin.readline().split()))
        sum = 0
        for elem in lst:
            sum += elem
        res.append(sum)

    for relem in res:
        print(relem)