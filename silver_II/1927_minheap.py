# -*- coding: utf-8 -*-
from sys import stdin
import heapq

if __name__ == "__main__":
    n = int(stdin.readline().rstrip())

    minh = []
    for i in range(n):
        num = int(stdin.readline().rstrip())
        if num == 0:
            try:
                min_num = heapq.heappop(minh)
                print(min_num)
            except IndexError:
                print(0)
        else:
            heapq.heappush(minh, num)
