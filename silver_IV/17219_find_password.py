# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict

if __name__ == "__main__":
    inp, num_p = map(int, stdin.readline().split())

    book = defaultdict(str)
    for i in range(inp):
        site, pw = stdin.readline().rstrip().split()
        book[site] = pw

    res = []
    for j in range(num_p):
        site = stdin.readline().rstrip()
        res.append(book[site])

    for elem in res:
        print(elem)