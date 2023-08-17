# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    n = int(stdin.readline())

    sum = 0
    lst = []
    previdx = -1
    for i in range(n):
        toadd = int(stdin.readline())
        if toadd != 0:
            sum += toadd
            lst.append(toadd)
            previdx += 1
        else:
            sum -= lst[previdx]
            del lst[previdx]
            previdx -= 1

    print(sum)