# -*- coding:utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    lst = [i for i in range(1, 30+1)]

    for i in range(28):
        inp = int(stdin.readline().rstrip())
        lst.remove(inp)

    if lst[0] < lst[1]:
        print(lst[0])
        print(lst[1])
    else:
        print(lst[1])
        print(lst[0])