# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    a, b = map(int, stdin.readline().split())
    # print(a*a-b*b)
    print(pow(a, 2) - pow(b, 2))