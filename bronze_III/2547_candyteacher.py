# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    cases = int(stdin.readline())
    
    for i in range(cases):
        blank = stdin.readline()
        numstd = int(stdin.readline())
        sum = 0
        for j in range(numstd):
            sum += int(stdin.readline())

        if sum % numstd != 0:
            print('NO')
        else:
            print('YES')