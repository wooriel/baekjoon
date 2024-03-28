# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    num, cm = map(int, stdin.readline().split())

    trees = list(map(int, stdin.readline().split()))

    minh, maxh = 0, max(trees)
    while True:
        total = 0
        midh = (minh + maxh)//2
        if minh == midh or maxh == midh:
            break
        for elem in trees:
            total += max(elem - midh, 0)
        if total == cm:
            break
        elif total < cm:
            maxh = midh # cut more, height gets lower
        else:
            minh = midh

    print(midh)