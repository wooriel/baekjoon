# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict
from queue import PriorityQueue
import math

if __name__ == "__main__":
    n = int(stdin.readline())  # number of cities
    m = int(stdin.readline())  # number of buses

    edges = defaultdict(set)
    city = set()
    for i in range(m):
        s, e, c = map(int, stdin.readline().split())
        edges[s].add((c, e))
        city.add(s)
        city.add(e)

    start, end = map(int, stdin.readline().split())

    city_idx = dict()  # city_name : index in city_dist
    city_dist = []  # tracks shortest distance from the start
    for elem in enumerate(city):
        _idx, _city = elem
        city_idx[_city] = _idx
        city_dist.append(math.inf)
        if _city == start:
            city_dist[_idx] = 0

    next_edge = PriorityQueue()  # holds edges for the vertices included in the set
    next_edge.put((0, start))
    while next_edge.empty() == False:
        cost, cur = next_edge.get()  # popped cost should be total cost
        # update the cost of cur
        cur_idx = city_idx[cur]
        cur_dist = city_dist[cur_idx]

        if cur_dist < cost:
            continue

        for elem in edges[cur]:
            n_cost, n_elem = elem
            n_idx = city_idx[n_elem]
            pn_dist = city_dist[n_idx]
            n_dist = n_cost + cur_dist
            if pn_dist > n_dist:
                city_dist[n_idx] = n_dist
                next_edge.put((n_dist, n_elem))

    e_idx = city_idx[end]
    ans = city_dist[e_idx]
    print(ans)
