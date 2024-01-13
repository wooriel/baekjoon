# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    r, c = map(int, stdin.readline().split())

    lst = []
    for i in range(r):
        lst1 = list(map(int, stdin.readline().split()))
        lst.append(lst1)

    for j in range(r):
        lst2 = list(map(int, stdin.readline().split()))
        for k in range(c):
            lst[j][k] = str(lst2[k] + lst[j][k])
    
    for m in range(r):
        print(" ".join(lst[m]))