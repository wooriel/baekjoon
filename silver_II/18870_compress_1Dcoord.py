# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    n = int(stdin.readline().rstrip())
    lst = list(map(int, stdin.readline().split()))

    tups = [(lst[i], i) for i in range(n)]
    tups.sort(key=lambda x:x[0])

    count = 0
    lst[tups[0][1]] = count
    for i in range(1, n):
        if tups[i-1][0] == tups[i][0]:
            lst[tups[i][1]] = count
        else:
            count += 1
            lst[tups[i][1]] = count

    print(" ".join(str(lst[i]) for i in range(n)))