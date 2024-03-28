# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    n = int(stdin.readline())
    for i in range(n, 0, -1):
        text = '*'*i
        print(text)