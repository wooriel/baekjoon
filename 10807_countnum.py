# -*- coding:utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    n = int(stdin.readline().rstrip())
    lst = list(map(int, stdin.readline().split()))
    to_find = int(stdin.readline().rstrip())

    count = 0
    for elem in lst:
        if elem == to_find:
            count += 1

    print(count)