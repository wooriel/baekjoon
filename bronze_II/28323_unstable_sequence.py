# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    n = int(stdin.readline())
    lst = list(map(int, stdin.readline().split()))

    osta = []
    prev_o = 'e'
    esta = []
    prev_e = 'o'
    for i in range(n):
        cur = lst[i]
        cur_oe = cur % 2
        if cur_oe == 1 and prev_o == 'e':
            osta.append(cur)
            prev_o = 'o'
        elif cur_oe == 0 and prev_o == 'o':
            osta.append(cur)
            prev_o = 'e'
        if cur_oe == 1 and prev_e == 'e':
            esta.append(cur)
            prev_e = 'o'
        elif cur_oe == 0 and prev_e == 'o':
            esta.append(cur)
            prev_e = 'e'

    print(max(len(osta), len(esta)))
