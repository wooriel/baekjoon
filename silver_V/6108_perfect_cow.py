# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    n = int(stdin.readline())
    medians = []

    mid_idx = n//2
    for i in range(n):
        lst = list(map(int, stdin.readline().split()))
        lst.sort()
        medians.append(lst[mid_idx])

    medians.sort()
    print(medians[mid_idx])
