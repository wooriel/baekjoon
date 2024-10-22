# -*- coding: utf-8 -*-
from sys import stdin
from itertools import combinations


def is_not_neighbor(_idx, l_row, l_col):
    # receives 1D map and index of 1D
    visited = set()
    for elem in _idx:
        r = elem // l_col
        c = elem % l_col
        cur = (r, c)
        if cur not in visited:
            visited.add(cur)
            dr = [-1, 0, 1, 0]
            dc = [0, -1, 0, 1]
            for i in range(4):
                neigh = (r+dr[i], c+dc[i])
                if 0 <= neigh[0] < l_row and 0 <= neigh[1] < l_col:
                    if neigh not in visited:
                        visited.add(neigh)
        else:
            return False
    return True


def get_sum(_map, _idx):
    # receives 1D map and index of 1D
    _sum = 0
    for elem in _idx:
        _sum += _map[elem]

    return _sum


if __name__ == "__main__":
    n, m, k = map(int, stdin.readline().split())
    _map = []  # 1D map

    for i in range(n):
        lst = list(map(int, stdin.readline().split()))
        _map.extend(lst)

    _l = len(_map)
    _map_idx = [i for i in range(_l)]

    # get all combination of indices
    comb_lst = list(combinations(_map_idx, k))

    _max = -10000*k
    for elem in comb_lst:
        # check if neighbor does not exists
        if is_not_neighbor(elem, n, m):
            cur = get_sum(_map, elem)
            if cur > _max:
                _max = cur

    print(_max)
