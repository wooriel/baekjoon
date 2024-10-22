# -*- coding: utf-8 -*-
from sys import stdin
import math
from collections import defaultdict
# from collections import deque

if __name__ == "__main__":
    # _n: num_student, _m: directed_path, _x: destination
    _n, _m, _x = map(int, stdin.readline().split())
    _x -= 1

    # make 2D map for floyd-warshall algorithm
    _map = []
    for i in range(_n):
        _lst = [math.inf for j in range(_n)]
        _lst[i] = 0
        _map.append(_lst)

    # update the distance
    for j in range(_m):
        _s, _e, _c = map(int, stdin.readline().split())
        _s -= 1
        _e -= 1

        if _s != _e and (_map[_s][_e] == math.inf or _map[_s][_e] > _c):
            _map[_s-1][_e-1] = _c

    for m in range(_n):  # node that goes through
        for n in range(_n):  # starting node
            for k in range(_n):  # destination node
                if n != m and m != k and n != k:
                    if _map[n][k] > _map[n][m] + _map[m][k]:
                        _map[n][k] = _map[n][m] + _map[m][k]

    # dist = [0 for i in range(_n)]
    _max = _map[0][_x] + _map[_x][0]
    for l in range(1, _n):
        _val = _map[l][_x] + _map[_x][l]
        if _max < _val:
            _max = _val

    print(_max)
