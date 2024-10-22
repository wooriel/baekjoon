# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    m, t, u, f, d = map(int, stdin.readline().split())
    # m: allowed sec
    # t: unit of uphill, downhill, flatpath
    # u: sec that takes to go uphill per one unit of path
    # f: `` for flatpath
    # d: `` for downhill

    total = 0
    dist = 0
    flag = True
    for i in range(t):
        _inp = stdin.readline().rstrip()
        _cur = 0
        if flag:
            if _inp == 'u' or _inp == 'd':
                _cur = u + d
            else:
                _cur = f*2
            if _cur + total <= m:
                total += _cur
                dist += 1
            else:
                flag = False
        else:
            continue
        # if flag:
        #     if _inp == 'u' or _inp == 'd':
        #         _cur = (u + d)*t
        #     else:
        #         _cur = f*t*2
        #     if total + _cur <= m:
        #         total += _cur
        #         dist += t
        #     else:
        #         flag = False
        #         for j in range(t):
        #             _cur2 = 0
        #             if _inp == 'u' or _inp == 'd':
        #                 _cur2 = u + d
        #             else:
        #                 _cur2 = f*2
        #             if _cur2 + total <= m:
        #                 total += _cur2
        #                 dist += 1
        #             else:
        #                 break
        # else:
        #     continue

    print(dist)
