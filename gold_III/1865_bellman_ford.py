# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict
from collections import deque
import math


if __name__ == "__main__":
    _t = int(stdin.readline())

    for i in range(_t):
        node = defaultdict(list)
        _n, _m, _w = map(int, stdin.readline().split())
        for j in range(_m):  # positive edge
            _s, _e, _c = map(int, stdin.readline().split())
            node[_s].append((_e, _c))
            node[_e].append((_s, _c))
        for k in range(_w):  # negative edge
            _s, _e, _c = map(int, stdin.readline().split())
            node[_s].append((_e, -_c))

        flag = True
        # start from node 1
        dist = [math.inf for v in range(_n)]  # distance from node1
        dist[0] = 0
        # s = 1
        # while len(node[s]) == 0:
        #     dist[s-1] = math.inf
        #     s += 1
        #     dist[s-1] = 0

        node_vis = [0 for v in range(_n)]
        node_vis[0] = 1
        _break = False
        while _break == False:
            _break = True
            dist = [math.inf for v in range(_n)]
            for i in range(_n):
                if node_vis[i] == 0:
                    _break = False
                    node_vis[i] = 1
                    # for all non-visited node, check the distance.
                    dist[i] = 0
            for _v in range(_n):  # start from _v+1
                for v in range(_n):  # key
                    _cur = v+1
                    _cost = dist[_cur-1]
                    if _cost == math.inf:
                        continue
                    else:
                        for elem in node[_cur]:
                            _e, _c = elem
                            if dist[_e-1] > _cost+_c:  # dist[_e-1] != math.inf and
                                dist[_e-1] = _cost+_c
                                node_vis[_e-1] = 1
                                # if _e not in visited:
                                # to_check.append(_e)
                                # visited.add(_e)
                                if _v == _n-1:
                                    flag = False
                                    break

        if flag:
            print('NO')
        else:
            print('YES')
