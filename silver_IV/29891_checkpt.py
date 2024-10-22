# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    n, k = map(int, stdin.readline().split())

    total = 0
    below_zero = []
    above_zero = []
    for i in range(n):
        x = int(stdin.readline())
        if x < 0:
            below_zero.append(-x)
        elif x > 0:
            above_zero.append(x)
    below_zero.sort()
    above_zero.sort()
    baddpt = len(below_zero) % k - 1
    aaddpt = len(above_zero) % k - 1
    if baddpt < 0:
        baddpt += k
    if aaddpt < 0:
        aaddpt += k
    for i in range(baddpt, len(below_zero), k):
        total += below_zero[i]*2
    for i in range(aaddpt, len(above_zero), k):
        total += above_zero[i]*2

    print(total)
