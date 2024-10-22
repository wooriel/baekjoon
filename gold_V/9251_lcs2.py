# -*- coding: utf-8 -*-
from sys import stdin


if __name__ == "__main__":
    a = stdin.readline().rstrip()
    b = stdin.readline().rstrip()
    l_a = len(a)
    l_b = len(b)

    _map = []
    for i in range(l_a):
        lst = [0 for j in range(l_b)]
        _map.append(lst)

    _min = (0, 0)
    for i in range(l_a):
        for j in range(l_b):
            if a[i] == b[j]:
                _map[i][j] = 1
                if i != 0 and j != 0:
                    _map[i][j] += _map[i-1][j-1]
            else:
                _map[i][j] = max(_map[i-1][j], _map[i][j-1])

    print(_map[-1][-1])
