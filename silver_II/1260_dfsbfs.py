# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict
from collections import deque

def bfs(tree, num_node, start):
    # returns order:list
    order = []
    visited = set()
    _stack = deque([])

    cur_node = start
    for i in range(num_node):
        order.append(str(cur_node))
        visited.add(cur_node)

        linked_nds = sorted(list(set(tree[cur_node]) - visited)) #
        # order.extend(linked_nds)
        _stack.extend(sorted(list(set(linked_nds)-set(_stack))))

        try:
            cur_node = _stack.popleft()
        except IndexError:
            # assert i == num_node - 1 <- graph not connected
            break

    return order


def dfs_helper(tree, order, visited, cur_node):
    order.append(str(cur_node))
    visited.add(cur_node)

    to_visit = sorted(list(set(tree[cur_node]) - visited))
    try:
        # cur_node = to_visit[0]
        for i in range(len(to_visit)):
            cur_node = to_visit[i]
            if cur_node not in visited:
                dfs_helper(tree, order, visited, cur_node)
            else:
                continue
    except IndexError:
        return


def dfs(tree, start):
    order = []
    visited = set()

    dfs_helper(tree, order, visited, start)
    return order


if __name__ == "__main__":
    n, e, start = map(int, stdin.readline().split())

    edges = defaultdict(list)
    for i in range(e):
        s, e = map(int, stdin.readline().split())
        edges[s].append(e)
        edges[e].append(s)

    # dfs를 위해 따로 처리
    if e == 0:
        edges[start] = []

    n = len(edges.keys())
    for elem in edges.keys():
        edges[elem] = sorted(edges[elem])

    order1 = dfs(edges, start)
    order2 = bfs(edges, n, start)

    print(" ".join(order1))
    print(" ".join(order2))