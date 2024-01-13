# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict

def cal_dict(num):
    dict123 = defaultdict(int)
    dict123[0] = 0
    dict123[1] = 1
    dict123[2] = 2
    dict123[3] = 4
    for i in range(4, num+1):
        dict123[i] = dict123[i-1] + dict123[i-2] + dict123[i-3]

    return dict123


if __name__ == "__main__":
    n = int(stdin.readline().rstrip())

    inp = []
    for i in range(n):
        inp.append(int(stdin.readline().rstrip()))

    max_inp = max(inp)
    d = cal_dict(max_inp)

    for i in range(n):
        print(d[inp[i]])