# -*- coding: utf-8 -*-
import sys
from sys import stdin
sys.setrecursionlimit(10**6)
from collections import defaultdict

# fdict = defaultdict(int)
# fdict[1] = 1
# fdict[2] = 2
# def fibo(n):
#     if n in fdict:
#         return fdict[n]
#     else:
#         fdict[n] = (fibo(n-1) + fibo(n-2)) % 15746
#         return fdict[n]

if __name__ == "__main__":
    n = int(stdin.readline())

    # print(fibo(n) % 15746)


    fibo = [1, 2]
    if n > 2:
        for i in range(2, n):
            fibo.append((fibo[i-1] + fibo[i-2]) % 15746)

    print(fibo[n-1] % 15746)

    
    # fdict = defaultdict(int)
    # fdict[1] = 1
    # fdict[2] = 1
    # def fibo(n):
    #     if n in fdict:
    #         return fdict[n]
    #     else:
    #         fdict[n] = fibo(n-1) + fibo(n-2)
    #         return fdict[n]

    # print(fibo(n) % 15746)
        
    # cases = n // 2
    # mod = n % 2

    # sum = 0
    # n00 = cases
    # n1 = 1 if mod == 1 else 0
    # for i in range(cases):
    #     sum += comb(n00 + n1, n1)
    #     n00 -= 1
    #     n1 += 2
    # sum += 1

    # print(sum % 15746)