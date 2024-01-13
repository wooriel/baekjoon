# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict
from collections import deque

def traverse_all(tree:dict):
    
    visited = set()


if __name__ == "__main__":
    v, e = map(int, stdin.readline().split())

    neigh = defaultdict()
    for i in range(e):
        a, b = map(int, stdin.readline().split())
        neigh[a] = b
        neigh[b] = a

    num_g = traverse_all(neigh)