# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict
from queue import PriorityQueue
import math


def dijk(sta, end, edge, _n):
    dist = [math.inf for i in range(_n)]
    prev = [-1 for i in range(_n)]
    dist[sta] = 0
    node = PriorityQueue()
    node.put((0, sta, -1))
    while node.empty() == False:
        _c, _e, _p = node.get()
        if dist[_e] > _c:
            dist[_e] = _c
            # update path
            prev[_e] = _p
        else:
            # if end is reached, break
            if _e == end:
                break
        for elem in edge[_e]:
            n_c = elem[0] + _c
            if dist[elem[1]] > n_c:
                node.put((n_c, elem[1], _e))

    return dist, prev


if __name__ == "__main__":
    _n = int(stdin.readline())
    _m = int(stdin.readline())

    # default val: -1, maps name of city into index
    name_idx = defaultdict(lambda: -1)
    idx_name = defaultdict(lambda: -1)
    _idx = 0
    edge = defaultdict(list)
    # visited = set()
    for i in range(_m):
        _s, _e, _c = map(int, stdin.readline().split())
        if name_idx[_s] == -1:
            name_idx[_s] = _idx
            idx_name[_idx] = _s
            _idx += 1
        if name_idx[_e] == -1:
            name_idx[_e] = _idx
            idx_name[_idx] = _e
            _idx += 1
        if _s != _e:
            # if (_s, _e) not in visited:
            edge[name_idx[_s]].append([_c, name_idx[_e]])
            # visited.add((_s, _e))
            # else:
            #     nidx = name_idx[_s]
            #     for j in range(len(edge[nidx])):
            #         elem = edge[nidx][j]
            #         if elem[1] == _e and elem[0] > _c:
            #             edge[nidx][j][0] = _c

    start, end = map(int, stdin.readline().split())

    _dist, _prev = dijk(name_idx[start], name_idx[end], edge, _n)

    print(_dist[name_idx[end]])

    # print path
    path = []
    path.append(end)
    _next = _prev[name_idx[end]]  # index of previous node
    while _next != name_idx[start]:
        path.append(idx_name[_next])
        _next = _prev[_next]
    path.append(start)

    print(len(path))

    while len(path) > 0:
        elem = path.pop()
        if len(path) > 0:
            print(elem, end=' ')
        else:
            print(elem)
