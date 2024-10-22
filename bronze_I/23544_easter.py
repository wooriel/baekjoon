# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict

if __name__ == "__main__":
    n = int(stdin.readline())

    hippo = defaultdict(int)
    for i in range(n):
        _str = stdin.readline().rstrip()
        hippo[_str] += 1

    _key = list(hippo.keys())
    print(n - len(_key))
