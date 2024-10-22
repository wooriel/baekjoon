# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict
from collections import deque


def bfs(s_node, e_dict):
    nodes = deque()
    nodes.append((s_node, 0))  # node, distance
    visited = set()
    m_node = (s_node, 0)
    visited.add(s_node)  # 79% error
    while len(nodes) > 0:
        _cur, _weight = nodes.popleft()
        if _weight > m_node[1]:
            m_node = (_cur, _weight)
        for elem in e_dict[_cur]:
            n_node, n_w = elem
            if n_node not in visited:
                visited.add(n_node)
                nodes.append((n_node, n_w+_weight))
    return m_node


if __name__ == "__main__":
    _num = int(stdin.readline())

    edge = defaultdict(list)

    for i in range(_num-1):
        _d, _c, _w = map(int, stdin.readline().split())
        edge[_d].append((_c, _w))  # 중복에 더 큰 간선이 있을지는 의문
        edge[_c].append((_d, _w))

    # non_overlap = defaultdict(int)
    # for i in range(_num-1):
    #     _d, _c, _w = map(int, stdin.readline().split())
    #     if non_overlap[(_d, _c)] < _w:
    #         non_overlap[(_d, _c)] = _w

    # _key = list(non_overlap.keys())
    # for i in range(len(_key)):
    #     _d, _c = _key[i]
    #     _w = non_overlap[(_d, _c)]
    #     edge[_d].append((_c, _w))  # 중복에 더 큰 간선이 있을지는 의문
    #     edge[_c].append((_d, _w))

    # from node 1, find the longest path using bfs (it can be any node)
    max_end = bfs(1, edge)
    # max_end edge is one end of longest diameter..?
    new_end = bfs(max_end[0], edge)
    print(new_end[1])
    # while True:
    #     new_end = bfs(max_end[0], edge)
    #     if max_end[1] == new_end[1]:
    #         break
    #     else:
    #         max_end = new_end

    # print(max_end[1])
