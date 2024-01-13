# -*- coding: utf=8 -*-
from sys import stdin
from collections import defaultdict
from collections import deque

if __name__ == "__main__":
    num_node = int(input())
    num_edge = int(input())

    con_com = defaultdict(set)

    for i in range(num_edge):
        s, e = map(int, stdin.readline().split())
        con_com[s].add(e)
        con_com[e].add(s)

    virus = deque()
    virus.append(1)
    visited = set()
    visited.add(1)
    count = 0
    while len(virus) != 0:
        cur = virus.popleft()
        count += 1
        # visited.add(cur)
        to_add = con_com[cur] - visited
        virus.extend(list(to_add))
        visited = visited.union(to_add)

    print(count - 1)
