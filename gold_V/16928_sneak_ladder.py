# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict
from collections import deque

if __name__ == "__main__":
    ladder, sneak = map(int, stdin.readline().split())

    warp = dict()

    for i in range(ladder):
        s, e = map(int, stdin.readline().split())
        warp[s] = e

    for j in range(sneak):
        s, e = map(int, stdin.readline().split())
        warp[s] = e


    cur_pos = deque()
    cur_pos.append((1, 0))
    node_count = defaultdict(int)
    while len(cur_pos) > 0:
        num, count = cur_pos.popleft()
        ncount = count + 1
        for i in range(num+6, num, -1):
            # check if there is sneak or ladder
            new_node = i
            while new_node in warp:
                new_node = warp[new_node]
            # add in node_count
            if node_count[new_node] == 0:
                node_count[new_node] = ncount
                cur_pos.append((new_node, ncount))
            else:
                if ncount < node_count[new_node]:
                    node_count[new_node] = ncount
        if node_count[100] != 0:
            break

    print(node_count[100])