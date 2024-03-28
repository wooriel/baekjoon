# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict
from collections import deque

if __name__ == "__main__":
    num_ppl = int(stdin.readline())
    nlst = {i for i in range(1, num_ppl+1)}

    node1, node2 = map(int, stdin.readline().split())

    num_edge = int(stdin.readline())
    p_c = defaultdict(list) # parent's child
    c_p = dict() # child's parent
    for i in range(num_edge):
        p, c = map(int, stdin.readline().split())
        p_c[p].append(c)
        c_p[c] = p
        
    nodes = deque()
    nodes.append((node1, 0))
    visited = set()

    ans = -1
    while len(nodes) > 0:
        cur_node, dist = nodes.popleft()
        if cur_node == node2:
            ans = dist
            break
        # add to visited
        visited.add(cur_node)
        # append parent
        if c_p.get(cur_node) is not None:
            parent = c_p[cur_node]
            if parent not in visited:
                nodes.append((c_p[cur_node], dist+1))
        # append childs
        child_lst = p_c[cur_node]
        for elem in child_lst:
            if elem not in visited:
                nodes.append((elem, dist+1))
    
    print(ans)