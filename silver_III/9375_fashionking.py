# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict
from itertools import combinations

if __name__ == "__main__":
    cases = int(stdin.readline().rstrip())
    
    for i in range(cases):
        num_clothes = int(stdin.readline().rstrip())
        drawer = defaultdict(int)

        for j in range(num_clothes):
            name, kind = stdin.readline().rstrip().split()
            drawer[kind] += 1

        val = list(drawer.values())
        # val = [3, 5, 2, 7]
        total = 1
        for elem in val:
            total *= (elem+1)
        print(total - 1)
        
        # subsets = []
        # subsets.append([])
        # for elem in val:
        #     size = len(subsets)
        #     for i in range(size):
        #         cur = subsets[i].copy()
        #         if len(cur) == 0:
        #             cur.append(elem)
        #         else:
        #             cur = [cur[0] * elem]
        #         subsets.append(cur)

        # total = 0
        # subsets.pop(0)
        # for elem in subsets:
        #     total += elem[0]

        # print(total)