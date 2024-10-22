# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    a, b, r = map(int, stdin.readline().split())
    if a > r and b > 1:
        print("overflow")
    elif b > r and a > 1:
        print("overflow")
    elif a == 0 or b == 0:
        print(0)
    else:
        mul = a*b
        if mul > r:
            print("overflow")
        else:
            print(mul)
