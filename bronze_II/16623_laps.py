# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    n, m = map(int, stdin.readline().split())
    lst = list(map(int, stdin.readline().split()))

    laps = 0
    for i in range(1, m):
        if lst[i-1] > lst[i]:
            laps += 1

    print(laps)
