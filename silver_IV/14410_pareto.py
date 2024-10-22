# -*- coding: utf-8 -*-
from sys import stdin


def _sum(lst):
    sum = 0
    for elem in lst:
        sum += elem
    return sum


if __name__ == "__main__":
    n = int(stdin.readline())
    lst = list(map(int, stdin.readline().split()))
    lst.sort(reverse=True)

    a, num_b = 0, 0
    total = _sum(lst)
    _amax, _bmax = 0, 0
    for i in range(n):
        a = (i+1)/n * 100  # total certain percent of people
        num_b += lst[i]
        b = num_b/total*100
        if b-a > _bmax-_amax:
            _amax = a
            _bmax = b
        else:
            break

    print(_amax)
    print(_bmax)
