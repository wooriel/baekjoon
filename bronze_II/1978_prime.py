# -*- coding: utf-8 -*-

def is_prime(n):
    if n == 1:
        return 0
    else:
        for i in range(2, n):
            if n % i == 0:
                return 0
        return 1

if __name__ == "__main__":
    num = int(input())
    lst = list(map(int, input().split()))

    num_prime = 0
    for i in range(num):
        num_prime += is_prime(lst[i])

    print(num_prime)