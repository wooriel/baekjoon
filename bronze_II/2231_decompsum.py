# -*- coding: utf-8 -*-
from sys import stdin

def decomp_sum(n: int):
    strnum = str(n)

    strsum = 0
    for i in range(len(strnum)):
        strsum += int(strnum[i])

    return strsum + n

if __name__ == "__main__":
    dsum = int(stdin.readline()) # output의 분해합

    m = 0
    for i in range(dsum):
        if decomp_sum(i) == dsum:
            m = i
            break

    print(m)
