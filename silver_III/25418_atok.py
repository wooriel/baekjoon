# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque

if __name__ == "__main__":
    a, k = map(int, stdin.readline().split())

    # lst = [0 for i in range(a, k+1)]

    cnt = 0
    while k // 2 >= a:
        if k % 2 == 0:
            k = k // 2
            cnt += 1
        else:
            k -= 1
            k = k // 2
            cnt += 2
    cnt += k-a

    print(cnt)
