# -*- coding:utf-8 -*-

if __name__ == "__main__":
    n = int(input())

    if n == 0 or n == 1:
        print(1)
    else:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        print(fact)
