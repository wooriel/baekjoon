# -*- coding: utf-8 -*-
from sys import stdin
from math import comb
from math import perm

if __name__ == "__main__":
    num = int(stdin.readline())

    num_tab = num//2
    mult = 1
    for i in range(num_tab):
        mult *= comb(num, 2)
        num -= 2
    
    print(mult // perm(num_tab))