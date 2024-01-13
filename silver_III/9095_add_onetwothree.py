# -*- coding: utf-8 -*-
from sys import stdin
from math import comb
from math import perm

def cal_cases(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        quot = num // 3
        rem = num % 3 # rem + 1 indicates where 3 can get in
        poss = 0
        for i in range(1, quot+1):
            # three and ones
            num1 = (quot - i)*3 + rem
            poss += comb(num1 + i, i)
            # # when 3 divided into 2 and 1
            num1_for2 = num1
            for j in range(1, i+1):
                num1_for2 += 1
                poss += comb(i + num1_for2, i) * comb(i, j)
                num2 = num1_for2 // 2
                if i == quot and num2 > 0:
                    num1_for22 = num1_for2
                    for l in range(1, num2 + 1):
                        num1_for22 -= 2
                        poss += comb(i + num1_for22 + l, i+l) * comb(i+l, j+l)
        if rem == 2:
            poss += comb(quot+1, quot)
        return poss + 1 # all 1

if __name__ == "__main__":
    res = []
    # n = 7
    # cal_cases(7)
    cases = int(stdin.readline().rstrip())
    for i in range(cases):
        n = stdin.readline().rstrip()
        res.append(cal_cases(int(n)))

    for elem in res:
        print(elem)