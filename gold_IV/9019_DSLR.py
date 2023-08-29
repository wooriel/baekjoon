# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict
from enum import Enum

class Operation(Enum):
    DOUBLE = 'D'
    SUBTRACT = 'S'
    LEFT = 'L'
    RIGHT = 'R'

class BFSGraph:
    def __init__(self, s, e):
        self.s = s
        self.e = e
        self.path = []

        self.visited = set()
        
        self.graph = defaultdict(lambda: 'N')
        self.power = 0
        self.idx = 0
        # self.add_graph(self.s, self.idx)

    def is_visited(self, num):
        return num in self.visited
    
    def add_visited(self, num):
        self.visited.add(num)

    def add_graph(self, num, oper):
        self.graph[num] = oper

    def get_parent(self, idx):
        pidx = idx//4
        return self.graph[pidx]

    def get_double(self, num):
        return num * 2 % 10000
    
    
    def get_sub(self, num):
        return 9999 if num == 0 else num - 1
    
    def get_left(self, num):
        return (num % 1000) * 10 + num // 1000
    
    def get_right(self, num):
        return (num % 10) * 1000 + (num // 10)
    
    # def is_end(self, idx):
    #     if self.e == self.graph[idx]:
    #         return True
    #     else:
    #         return False
        
    def is_end(self, num):
        return self.e == num
        
    def get_path(self, idx):
        p = ""
        while idx != 0:
            rem = idx % 4
            if rem == 0:
                p = "R" + p
            elif rem == 1:
                p = "D" + p
            elif rem == 2:
                p = "S" + p
            else:
                p = "L" + p
            idx = (idx - 1) // 4
        return p
    
    def cal_end(self, path):
        n = self.s
        for p in range(len(path)):
            flag = path[p]
            if flag == 'D':
                n = self.get_double(n)
            elif flag == 'S':
                n = self.get_sub(n)
            elif flag == 'L':
                n = self.get_left(n)
            else:
                n = self.get_right(n)

        return n

def cal_path(s, e):
    graph = BFSGraph(s, e)

    # count = 0
    while True:
        num = graph.get_parent(graph.idx)
        if num == -1:
            graph.idx += 4
        else:
            double = graph.get_double(num)
            graph.idx += 1
            if graph.is_visited(double):
                # graph.add_graph(None)
                continue
            else:
                # graph.idx += 1
                graph.add_graph(double, graph.idx)
                graph.add_visited(double)
            if graph.is_end(double):
                graph.path.append(graph.get_path(graph.idx))
                break
            
            sub = graph.get_sub(num)
            graph.idx += 1
            if graph.is_visited(sub):
                continue
            else:
                graph.add_graph(sub, graph.idx)
                graph.add_visited(sub)
            if graph.is_end(sub):
                graph.path.append(graph.get_path(graph.idx))
                break

            left = graph.get_left(num)
            graph.idx += 1
            if graph.is_visited(left):
                continue
            else:
                graph.add_graph(left, graph.idx)
                graph.add_visited(left)
            if graph.is_end(left):
                graph.path.append(graph.get_path(graph.idx))
                break

            right = graph.get_right(num)
            graph.idx += 1
            if graph.is_visited(right):
                continue
            else:
                graph.add_graph(right, graph.idx)
                graph.add_visited(right)
            if graph.is_end(right):
                graph.path.append(graph.get_path(graph.idx))
                break

    path = graph.path[0]
    # end_num = graph.cal_end(path) # to check
    return path


if __name__ == "__main__":
    n = int(stdin.readline())

    res = []
    for i in range(n):
        a, b = map(int, stdin.readline().split())
        path = cal_path(a, b)
        res.append(path)

    for elem in res:
        print(elem)