# -*- coding: utf-8 -*-
# import sys
# sys.setrecursionlimit(10**6)
from sys import stdin

# def help_tree(c, coin):
#     if c == 0:
#         return 1
#     elif c < 0:
#         return 0
#     else:
#         count = 0
#         for i in range(len(coin)):
#             count += help_tree(c-coin[i], coin[i:])
#         return count

# def tree(c, coin):
#     total = 0
#     for i in range(len(coin)):
#         total += help_tree(c-coin[i], coin[i:])

#     return total


if __name__ == "__main__":
    n, k = map(int, stdin.readline().split())

    coin = [0]
    for i in range(n):
        c = int(stdin.readline())
        if c <= k:
            coin.append(c)
        else:
            n -= 1

    coin.sort() # 왜 필요한거지???

    dp = [0 for m in range(k + 1)]
    dp[0] = 1

    for i in range(1, n+1):
        for j in range(i, k+1):
            if j - coin[i] >= 0:
                dp[j] += dp[j - coin[i]]

    print(dp[-1])

    # lst = []
    # case = 0
    # for i in range(n):
    #     lst.append(int(stdin.readline()))
    
    # lst.sort()

    # num = tree(k, lst)
    # print(num)

    