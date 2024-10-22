# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict
from collections import deque


def bfs(_s, e_dict):
    s_node = (_s, 0)
    to_visit = deque()
    to_visit.append(s_node)
    visited = set()
    visited.add(_s)
    m_node = (_s, 0)
    while len(to_visit) > 0:
        c_node, c_weight = to_visit.popleft()
        if m_node[1] < c_weight:
            m_node = (c_node, c_weight)
        for elem in e_dict[c_node]:
            n_node, n_w = elem
            if n_node not in visited:
                visited.add(n_node)
                to_visit.append((n_node, c_weight+n_w))

    return m_node


if __name__ == "__main__":
    n = int(stdin.readline())

    edge = defaultdict(list)
    for i in range(n):
        lst = list(map(int, stdin.readline().split()))
        _s = lst[0]
        for j in range(1, len(lst)-1, 2):
            _c, _w = lst[j], lst[j+1]
            edge[_s].append((_c, _w))

    max_node = bfs(1, edge)
    new_node = bfs(max_node[0], edge)

    print(new_node[1])
