# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict
import math
from queue import PriorityQueue

if __name__ == "__main__":
    _v, _e = map(int, stdin.readline().split())
    k = int(stdin.readline())

    edge = defaultdict(set)
    for i in range(_e):
        u, v, w = map(int, stdin.readline().split())
        edge[u].add((w, v))

    vert_dist = [math.inf for i in range(_v)]
    s_idx = k-1
    vert_dist[s_idx] = 0

    dist_node = PriorityQueue()
    dist_node.put((0, k))
    while dist_node.empty() == False:
        cur_cost, cur_node = dist_node.get()
        cur_idx = cur_node-1
        cur_dist = vert_dist[cur_idx]

        if cur_dist < cur_cost:
            continue

        for elem in edge[cur_node]:
            n_cost, n_node = elem
            n_idx = n_node-1
            p_dist = vert_dist[n_idx]
            n_dist = n_cost + cur_cost

            if p_dist > n_dist:
                vert_dist[n_idx] = n_dist
                dist_node.put((n_dist, n_node))

    for elem in vert_dist:
        if elem == math.inf:
            print('INF')
        else:
            print(elem)
