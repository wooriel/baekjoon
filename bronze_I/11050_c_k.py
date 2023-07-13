# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n, k = map(int, input().split())

    res = 1
    for i in range(1, n+1):
        res *= i

    for j in range(1, k+1):
        res /= j

    for m in range(1, n-k+1):
        res /= m

    print(int(res))