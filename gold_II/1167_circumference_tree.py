# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict
from collections import deque

if __name__ == "__main__":
    num_vert = int(stdin.readline())

    neighbors = defaultdict(list)
    for i in range(1, num_vert+1): # i = number of vertex
        lst = list(map(int, stdin.readline().split()[1:-1]))
        for i in range(0, len(lst), 2):
            neighbors[i].append(lst[i:i+2])
    
    # 각 vert에 대해서 depth를 구할 예정
    for i in range(1, num_vert+1): 
        visited = set()
        cur = i
        next_deque = deque()