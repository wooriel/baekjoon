# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    n, m = map(int, stdin.readline().split())
    lst = [1]
    for i in range(1, n+1):
        val = lst[i-1]
        if i - m >= 0:
            val += lst[i-m]
        lst.append(val)

    print(lst[-1] % 1000000007)
