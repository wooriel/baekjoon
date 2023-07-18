# -*- coding: utf-8 -*-
from collections import defaultdict

if __name__ == "__main__":
    n = int(input())
    
    nlst = list(map(int, input().split()))

    m = int(input())

    # {} for k, v in iterable
    mdict = defaultdict(int, map(0, [int(k) for k in input().split()]))

    for elem in nlst:
        if elem in mdict:
            if elem in mdict:
                mdict[elem] = 1

    for elem in mdict:
        if elem in mdict:
            print(str(mdict[elem]), end=" ")
        else:
            print('0', end=" ")

    # print(" ".join(str(v) for v in mdict.values()))