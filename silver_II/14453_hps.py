# -*- coding: utf-8 -*-
from sys import stdin


def update(_fj, prev: list):
    if 'H' == _fj:  # paper slot
        lst[0][0] += 1
        if lst[0][1] == -1:
            lst[0][1] = max(lst[1][0], lst[2][0])+1
        else:
            lst[0][1] = max(lst[1][0], lst[2][0], lst[0][1])+1
    elif 'S' == _fj:  # hoof slot (rock)
        lst[1][0] += 1
        if lst[1][1] == -1:
            lst[1][1] = max(lst[0][0], lst[2][0])+1
        else:
            lst[1][1] = max(lst[0][0], lst[2][0], lst[1][1])+1
    else:  # 'P' == _fj: # scissor slot
        lst[2][0] += 1
        if lst[1][1] == -1:
            lst[2][1] = max(lst[0][0], lst[1][0])+1
        else:
            lst[2][1] = max(lst[0][0], lst[1][0], lst[2][1])+1

    return prev


if __name__ == "__main__":

    n = int(stdin.readline())

    _fj = stdin.readline().rstrip()
    lst = [[0, -1], [0, -1], [0, -1]]
    if _fj == 'H':
        lst[0][0] += 1
    elif _fj == 'S':
        lst[1][0] += 1
    else:
        lst[2][0] += 1
    for i in range(1, n):
        _fj = stdin.readline().rstrip()
        update(_fj, lst)

    print(max(max(lst[0]), max(lst[1]), max(lst[2])))
