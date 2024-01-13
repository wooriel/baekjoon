# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    num_track, k = map(int, stdin.readline().split())

    lst = list(map(int, stdin.readline().rstrip().split()))

    flag = True
    num_k = 0
    cur = lst[0]
    for i in range(1, num_track):
        if cur >= lst[i]:
            if cur < lst[i] + k:
                lst[i] += k
                num_k += 1
            else:
                flag = False
                break
        cur = lst[i]

    if flag:
        print(num_k)
    else:
        print(-1)