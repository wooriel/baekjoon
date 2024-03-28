# -*- coding: utf-8 -*-
from sys import stdin

def gcd(a, b): # a > b
    while b != 0:
        a, b = b, a % b
    return abs(a)

if __name__ == "__main__":
    num = int(stdin.readline())
    plst = map(int, stdin.readline().split())
    blst = map(int, stdin.readline().split())

    psum = sum(plst)
    bsum = sum(blst)

    _gcd = gcd(psum, bsum)
    print("{} {}".format(bsum//_gcd, psum//_gcd))