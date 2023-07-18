# -*- coding: utf-8 -*-

from collections import deque

def is_vps(p):
    d = deque()

    for j in range(len(p)):
        if p[j] == '(':
            d.append('(')
        else:
            try:
                d.pop()
            except:
                return "NO"

    if d.count('(') != 0:
        return "NO"
    else:
        return "YES"


if __name__ == "__main__":
    n = int(input())

    lst = []
    for i in range(n):
        lst.append(is_vps(input()))

    for ans in lst:
        print(ans)