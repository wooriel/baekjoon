# -*- coding:utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    lst = []

    line = stdin.readline().rstrip()
    while line != "":
        lst.append(line)
        line = stdin.readline().rstrip()

    for elem in lst:
        print(elem)