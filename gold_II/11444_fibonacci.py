# -*- coding: utf-8 -*-
from collections import defaultdict
from sys import stdin
import sys
sys.setrecursionlimit(10**6)

#    f(n) = f(n-1) + f(n-2)
#        = f(n-2) + f(n-3) + f(n-2) = 2f(n-2) + f(n-3)
#         = 3f(n-3) + 2f(n-4)
#         = 5f(n-4) + 3f(n-5)
#         = f(6)*f(n-5) + f(5)*f(n-6)
#         = f(k+1)*f(n-k) + f(k)*f(n-(k+1))

#         f(0) = 0
#         f(1) = 1
#         f(2) = 1
#         f(3) = 2
#         f(4) = 3
#         f(5) = 5
#         f(6) = 8

#     # Put k=n/2
#     f(n) = f(n/2+1)f(n/2) + f(n/2)f(n/2-1)
#     # Put 2n instead of n in left side
#     f(2n) = f(n+1)f(n) + f(n)f(n-1)
#     f(2n+1) = f(n+1)f(n+1) + f(n)f(n)


def fib(n):
    global _lst
    global div
    # _lst = [0, 1]
    if n == 0:
        return 0
    elif _lst[n] != 0:
        return _lst[n] % div
    else:
        if n % 2 == 1:
            _val = (n-1)//2
            # return (fib(_val+1)*fib(_val+1) + fib(_val)*fib(_val)) % div
            _lst[n] = (fib(_val+1)*fib(_val+1) + fib(_val)*fib(_val)) % div
            return _lst[n]
        else:
            _val = n//2
            # return fib(_val)*(2*fib(_val-1) + fib(_val)) % div
            _lst[n] = fib(_val)*(2*fib(_val-1) + fib(_val)) % div
            return _lst[n]
            # return fib(_val+1)*fib(_val) % div + fib(_val)*fib(_val-1) % div


if __name__ == "__main__":
    n = int(stdin.readline())

    _lst = defaultdict(int)
    _lst[0] = 0
    _lst[1] = 1

    # _lst = [0, 1]
    div = 1000000007

    for i in range(2, 1000):
        _lst[i] = (_lst[i-1] + _lst[i-2]) % div

    print(fib(n) % div)

    # print(fib(n))
