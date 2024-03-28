# -*- coding: utf-8 -*-
from sys import stdin

# 최대공약수
def gcd(a, b):
    # a > b
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def lcm(a, b):
    if a > b:
        return a*b//gcd(a, b)
    else:
        return a*b//gcd(b, a)

if __name__ == "__main__":
    t_case = int(stdin.readline().rstrip())
    for i in range(t_case):
        m, n, x, y = map(int, stdin.readline().split())

        # 최소공배수
        max_yr = lcm(m, n)
        
        res = -1
        x_set = [m*i+x for i in range(max_yr//m)]
        for elem in x_set:
            if elem % n == y % n:
                res = elem

        print(res)