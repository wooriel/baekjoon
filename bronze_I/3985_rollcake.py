# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    l = int(stdin.readline())
    n = int(stdin.readline())

    roll = [0 for i in range(l)]
    max_exp = 0
    max_real = 0
    e_idx, r_idx = 0, 0
    for i in range(1, n+1):
        s, e = map(int, stdin.readline().split())

        _exp = e-s+1
        if max_exp < _exp:
            max_exp = _exp
            e_idx = i

        _real = 0
        for j in range(s-1, e):  # cake number starts from 1
            if roll[j] == 0:
                roll[j] = i
                _real += 1
        if max_real < _real:
            max_real = _real
            r_idx = i

    print(e_idx)
    print(r_idx)
