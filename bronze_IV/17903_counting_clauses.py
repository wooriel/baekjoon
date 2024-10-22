# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    m, n = map(int, stdin.readline().split())

    _set = set()
    for i in range(m):
        tup = tuple(map(int, stdin.readline().split()))
        _set.add(tup)

    if len(_set) < 8:
        print("unsatisfactory")
    else:
        print("satisfactory")
