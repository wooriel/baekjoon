# -*- coding: utf-8 -*-
from sys import stdin
import math

if __name__ == "__main__":
    a, b = map(int, stdin.readline().split())
    c, d = map(int, stdin.readline().split())
    k = int(stdin.readline())

    dol_count = (a+c)//d
    if (a+c) % d != 0:
        dol_count += 1
    if dol_count == 1:
        print(-1)
    else:
        toka = a
        move = b
        count = 0
        while count < dol_count:
            toka -= move
            move -= k
            count += 1
        if toka > 0:
            print(-1)
        else:
            print(count)
    # if dol_count == 1: # distance is more than 1
    #     print(-1)
    # else:
    #     # check if toka can get to home
    #     b_zero = b//k
    #     if b % k != 0:
    #         b_zero += 1
    #     pos_zero = a - b * b_zero + k * ((b_zero - 1) * (b_zero))//2
    #     if pos_zero > 0:
    #         print(-1)
    #     else:
    #         # check if toka can get to house with dol_count - 1
    #         toka_max = dol_count - 1
    #         home = a - b * toka_max + k * ((toka_max - 1) * (toka_max))//2
    #         if home == 0:
    #             print(home)
    #         elif home > 0:
    #             if dol_count >= b_zero:
    #                 print(-1)
    #             else:
    #                 toka = a
    #                 move = b
    #                 count = 0
    #                 while toka > 0:
    #                     toka -= move
    #                     move -= k
    #                     count += 1
    #                 # just check
    #                 if count >= dol_count:
    #                     print(-1)
    #                 else:
    #                     print(count)
    #         else:
    #             # count when becomes zero
    #             toka = a
    #             move = b
    #             count = 0
    #             while toka > 0:
    #                 toka -= move
    #                 move -= k
    #                 count += 1
    #             print(count) 