# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    k = int(stdin.readline())

    for i in range(1, k+1):
        n = int(stdin.readline())  # total number of water main breaks
        # [s, f] start and finish in range(sec)
        s, f = map(int, stdin.readline().split())

        _total = 0
        for j in range(n):
            s_i, f_i, r_i = map(int, stdin.readline().split())
            cur_f, cur_s = min(f, f_i), max(s, s_i)
            if cur_f >= cur_s:
                t_i = min(f, f_i) - max(s, s_i) + 1
                _total += t_i * r_i

        print("Data Set {}:".format(i))
        print(_total)
        if i != k:
            print("")
