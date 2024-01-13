# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict

if __name__ == "__main__":
    nhear, nsee = map(int, stdin.readline().split())

    groupnum = defaultdict(int)
    
    for i in range(nhear + nsee):
        nelem = input()
        groupnum[nelem] += 1

    names = list(groupnum.keys())
    count = 0
    res = []
    for j in range(len(names)):
        name = names[j]
        if groupnum[name] == 2:
            res.append(name)
            count += 1
    res.sort()
    print(count)
    for elem in res:
        print(elem)