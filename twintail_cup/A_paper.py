# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    half = int(stdin.readline())
    side = pow(half*2, 1/2)

    print(int(side)*4)