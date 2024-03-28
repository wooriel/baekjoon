# -*- coding: utf-8 -*-
from sys import stdin

def find_val(s):
    idx = 0
    rev = False
    val = True
    while s[idx] == '!':
        idx += 1
    if idx % 2 == 1:
        rev = True
    bidx = -1
    while s[bidx] == '!':
        bidx -= 1

    if s[idx] == '0':
        val = False
    if bidx < -1:
        val = True

    if rev:
        return not val
    else:
        return val


if __name__ == "__main__":
    num = int(stdin.readline())
    # lst = []
    for i in range(num):
        stat = stdin.readline().rstrip()
        val = find_val(stat)
        # lst.append(val)
        if val:
            print(1)
        else:
            print(0)