# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict

if __name__ == "__main__":
    n, m = map(int, stdin.readline().split())

    _map = []
    # apple = defaultdict(list)
    # block = defaultdict(list)
    apple = []
    for i in range(n):
        _lst = ['.' for k in range(m)]
        _str = stdin.readline().rstrip()
        for j in range(m):
            if _str[j] == '#':
                _lst[j] = '#'
                # block[j].append(i)
            elif _str[j] == 'o':
                _lst[j] = 'o'
                apple.append((i, j))
                # apple[j].append(i)
        _map.append(_lst)

    apple.sort(key=lambda x: x[0], reverse=True)

    for cur in apple:
        _r, _c = cur
        for i in range(_r, n-1):
            if _map[_r+1][_c] == '.':
                _r += 1
            else:
                break
        if _r != cur[0]:
            _map[_r][_c] = 'o'
            _map[cur[0]][_c] = '.'

    for i in range(n):
        print("".join(_map[i]))

    # for j in range(m):
    #     s = n-1
    #     for elem in block[j]:
    #         f = elem
    #         num_app = 0
    #         for app in apple[j]:
    #             if f < app <= s:  # f is where block is at
    #                 num_app += 1
    #         for i in range(num_app):
    #             _map[s+i][j] = 'o'
    #         s = f
    #     f = 0
    #     for app in apple[j]:
    #         if f <= app <= s:
    #             num_app += 1
    #     for i in range(num_app):
    #         # if s == n-1:
    #         #     _map[s+i][j] = 'o'
    #         # else:
    #         _map[s+i-1][j] = 'o'
