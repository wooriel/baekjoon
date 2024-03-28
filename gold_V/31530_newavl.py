# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    cases = int(stdin.readline())

    lst = []
    lst2 = []
    for i in range(cases):
        h, num_s = map(int, stdin.readline().split())
        set_s = set(map(int, stdin.readline().split()))

        
        if num_s == 1 or h == 1:
            print(1)
        elif num_s == 2:
            slot = 1
            for i in range(2, h):
                lst.append(slot * num_s)
                slot += 1
        # elif num_s == 2:
        #     print(pow(2, h-1)%(pow(10, 9)+7))
        # else:
        #     # pow(2, h-1): available slots
        #     # pow(2, pow(2, h-1)): sum of combinations
        #     # -1: empty set
        #     val = pow(pow(2, pow(2, h-2))) % (pow(10, 9)+7)
        #     print(val)