# -*- coding: utf-8 -*-
from sys import stdin
# from collections import defaultdict
import math
from copy import deepcopy


def _print(_m, n):
    for i in range(n):
        for j in range(n):
            if j == n-1:
                print("{}".format(_m[i][j]))
            else:
                print("{}".format(_m[i][j]), end=" ")


if __name__ == "__main__":
    n = int(stdin.readline())  # cities
    m = int(stdin.readline())  # buses

    _map = []
    for i in range(n):
        lst = [math.inf for j in range(n)]
        lst[i] = 0
        _map.append(lst)

    # bus = defaultdict(list)
    for i in range(m):
        s, e, c = map(int, stdin.readline().split())
        if c < _map[s-1][e-1]:
            _map[s-1][e-1] = c
        # bus[s].append((e, c))

    _next = deepcopy(_map)

    for k in range(n+1):  # check node 0 to n-1
        if k == n:
            for i in range(n):  # start
                for j in range(n):  # end
                    if _map[i][j] == math.inf:
                        _map[i][j] = 0
        else:
            for i in range(n):  # start
                for j in range(n):  # end
                    if i == k or j == k:
                        continue
                    else:
                        n_val = _map[i][k]+_map[k][j]
                        if n_val < _map[i][j]:
                            _next[i][j] = n_val
            _map = deepcopy(_next)

    _print(_map, n)
