# -*- coding: utf-8 -*-
from sys import stdin
import re

if __name__ == "__main__":
    pn = int(stdin.readline().rstrip())

    p_n = "I" + "OI" * pn
    strlen = int(stdin.readline().rstrip())
    iostr = stdin.readline().rstrip()

    p = re.compile(p_n)
    leng = len(p_n)
    sear = p.search(p_n)
    if sear == None:
        print(0)
    else:
        f_idx = sear.span()[0]
        count = 0
        while f_idx < strlen-leng+1:
            m = p.match(iostr[f_idx:f_idx+leng])
            if m != None:
                count += 1
                f_idx += 2
            else:
                f_idx += 1

        print(count)


    # p = re.compile(p_n)
    # iter = p.finditer(iostr)
    # count = 0
    # for elem in iter:
    #     count += 1
    #     s = elem.span()[0]
    #     leng = len(p_n)
    #     for j in range(s+2, min(s+leng, strlen), 2):
    #         if j+leng < strlen:
    #             if iostr[j:j+leng] == p_n:
    #                 count += 1
    # print(count)