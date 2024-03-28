# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    n = int(stdin.readline())
    lst = []
    lst.append(9)

    num0 = 0
    num9 = 1

    num1 = 1 # pnum0
    num8 = 1 # pnum9
    even_odd = [[num0, num9], [0, 0]] # n % 2 한게 index, turn on off like a switch
    while n > 1:
        num0 = n // 2
        cur = (lst[-1] - pnum0 - pnum9) * 2 + pnum0 + pnum9
        lst.append(cur)
        n -= 1

        

    print(lst[-1] % 1000000000)