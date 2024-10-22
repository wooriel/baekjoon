# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    while True:
        n = int(stdin.readline())
        if n == 0:
            break
        else:
            lst = list(map(int, stdin.readline().split()))

            avg = sum(lst)/n
            num = 0
            for i in range(n):
                if lst[i] <= avg:
                    num += 1

            print(num)
