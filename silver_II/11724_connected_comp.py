# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict
from collections import deque

def traverse_all(tree:dict):
    keys = set(tree.keys())
    
    num_comp = 0
    while len(keys) != 0:
        first_elem = list(keys)[0]

        to_trav = deque()
        to_trav.append(first_elem)
        visited = set()
        visited.add(first_elem)
        while len(to_trav) != 0:
            cur = to_trav.popleft()
            to_add = tree[cur] - visited
            for elem in list(to_add):
                if elem not in visited:
                    to_trav.append(elem)
                    visited.add(elem)
        keys -= visited
        num_comp += 1
        
    return num_comp


if __name__ == "__main__":
    v, e = map(int, stdin.readline().split())

    # if e == 0: #
    #     print(v)
    # else:
    neigh = defaultdict(set)
    for i in range(e):
        a, b = map(int, stdin.readline().split())
        neigh[a].add(b)
        neigh[b].add(a)

    num_g = traverse_all(neigh)
    just_vertex = v - len(list(neigh.keys()))

    print(num_g + just_vertex)