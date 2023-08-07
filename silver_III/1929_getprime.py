# -*- coding: utf-8 -*-
import math

def is_prime(num):
    if num % 2 == 0:
        return False
    else:
        for i in range(3, math.ceil(pow(num, 1/2)) + 1, 2):
            if num % i == 0:
                return False
        return True

if __name__ == "__main__":
    m, n = map(int, input().split())

    if m == 1:
        print(2)
        m += 2
    elif m == 2:
        print(2)
    if m % 2 == 0:
        m += 1
    for i in range(m, n+1, 2):
        if is_prime(i):
            print(i)