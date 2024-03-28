# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    x, y = map(int, stdin.readline().split())
    # x = ac^2 + bd^2
    # y = ab^2 + cd^2
    if y < x:
        print(-1)
    else:
        w = y/4 + (x-y)/2
        if w < 0:
            print(-1)
        else:
            print(round(2024*w))