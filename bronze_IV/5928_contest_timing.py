# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    d, h, m = map(int, stdin.readline().split())
    s = 11

    mval = m-s
    if mval < 0:
        h -= 1
        mval += 60
    hval = h-s
    if hval < 0:
        d -= 1
        hval += 24
    dval = d-s
    if dval < 0:
        print(-1)
    else:
        # calculate minute
        total = dval * 24 * 60 + hval * 60 + mval
        print(total)
