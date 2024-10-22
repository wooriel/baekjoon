# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict

if __name__ == "__main__":
    n = int(stdin.readline())

    for i in range(n):
        _str = stdin.readline().rstrip()

        alp = defaultdict(int)
        for j in range(len(_str)):
            _cur = _str[j]
            if _str[j].isalpha():
                alp[_cur] += 1

        _key = list(alp.keys())
        max_alp, max_occ = 0, 0
        cnt = 0
        for elem in _key:
            _cur = elem
            val = alp[elem]
            if max_occ < val:
                cnt = 0
                max_alp = elem
                max_occ = val
            elif max_occ == val:
                cnt += 1

        if cnt == 0:
            print(max_alp)
        else:
            print('?')
