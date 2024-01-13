# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    n, m = map(int, stdin.readline().split())
    print(abs(n - m))