# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    n = int(stdin.readline())

    lst = []

    for i in range(n):
        inptuple = tuple(map(int, stdin.readline().split()))
        lst.append(inptuple)

    lst.sort()
    lst.sort(key=lambda x: x[1])

    for j in range(n):
        print("{} {}".format(lst[j][0], lst[j][1]))