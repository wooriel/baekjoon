# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict

if __name__ == "__main__":
    nodes = int(stdin.readline())

    _map = []
    
    graph = defaultdict(set)
    for i in range(nodes):
        lst = list(map(int, stdin.readline().split()))
        for j in range(nodes):
            if lst[j] == 1:
                graph[i].add(j)
        mlst = ['0' for i in range(nodes)]
        _map.append(mlst)

    for i in range(nodes):
        for j in range(nodes):
            if i in graph[j]:
                _map[j][i] = '1'
                for elem in graph[i]:
                    _map[j][elem] = '1'
                    graph[j].add(elem)

    for i in range(nodes):
        print(" ".join(_map[i]))
            