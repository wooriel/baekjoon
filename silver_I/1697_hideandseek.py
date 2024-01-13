# -*- coding:utf-8 -*-
from sys import stdin
from collections import deque

def bfs_search(s, e):
    root = (s, 0)
    lst = deque()
    lst.append(root)
    visited = set()
    visited.add(s)
    pos = s
    cur_node = (s, 0)
    while pos != e:
        cur_node = lst.popleft()
        pos = cur_node[0]
        time = cur_node[1]
        plus = pos + 1
        minus = pos - 1
        warp = pos * 2
        plus_node, minus_node, warp_node = (plus, time + 1), (minus, time + 1), (warp, time + 1)
        if plus not in visited and plus <= 100000:
            lst.append(plus_node)
            visited.add(plus)
        if minus not in visited and minus >= 0:
            lst.append(minus_node)
            visited.add(minus)
        if warp not in visited and warp <= 100000:
            lst.append(warp_node)
            visited.add(warp)
    return cur_node[1]

if __name__ == "__main__":
    s, e = map(int, stdin.readline().split())
    t = bfs_search(s, e)
    print(t)
