# -*- coding: utf-8 -*-
from sys import stdin

# memoization
def tile(n):
    fibo = [1, 2]
    for i in range(2, n):
        fibo.append(fibo[i-1] + fibo[i-2])

    return fibo[-1]

if __name__ == "__main__":
    n = int(stdin.readline().rstrip())

    if n == 1 or n == 2:
        print(n)
    else:
        print(tile(n) % 10007)
