# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    while True:
        try:
            n = int(stdin.readline())

            num = 1
            for i in range(1, n+1):
                num *= i
                while num > 0 and num % 10 == 0:
                    num = num // 10

            print("{:5d} -> {}".format(n, str(num)[-1]))
            # print(str(num)[-1])
        except:
            break
