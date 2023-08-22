# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict

if __name__ == "__main__":
    n = int(stdin.readline())

    MAX_NUM = 10000

    dictionary = defaultdict(int)
    for i in range(n):
        toadd = int(stdin.readline())
        dictionary[toadd] += 1

    for j in range(1, MAX_NUM+1):
        for k in range(dictionary[j]):
            print(j)