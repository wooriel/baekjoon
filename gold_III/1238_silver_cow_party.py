from sys import stdin
from queue import PriorityQueue
# from collections import deque
from collections import defaultdict
import math


def dijk(sta, edge, _n):

    p_que = PriorityQueue()
    for elem in edge[sta]:
        p_que.put(elem)

    dist = [math.inf for i in range(_n)]
    dist[sta] = 0
    # visited = set()
    # visited.add(sta)
    while p_que.empty() == False:
        _c, _e = p_que.get()
        # _cost = dist[_s]
        # _val = _cost + _c  # from _s to _e
        if dist[_e] > _c:
            dist[_e] = _c
            for elem in edge[_e]:
                # update cost as current cost(_c) + edge cost
                n_c = elem[0]+_c
                if dist[elem[1]] > n_c:
                    p_que.put([n_c, elem[1]])

    return dist


if __name__ == "__main__":
    _n, _m, _x = map(int, stdin.readline().split())

    p_edge = defaultdict(list)
    f_edge = defaultdict(list)  # all the directed edges are flipped
    for i in range(_m):
        _s, _e, _c = map(int, stdin.readline().split())
        if _s != _e:  # skip the path to itself
            p_edge[_s-1].append([_c, _e-1])  # s-1
            f_edge[_e-1].append([_c, _s-1])

    # distance from _x to all the other points
    dist_fmx = dijk(_x-1, p_edge, _n)
    # p_edge = f_edge
    dist_tox = dijk(_x-1, f_edge, _n)

    _max = 0
    for i in range(_n):
        _cur = dist_tox[i] + dist_fmx[i]
        if _cur > _max:
            _max = _cur

    print(_max)
