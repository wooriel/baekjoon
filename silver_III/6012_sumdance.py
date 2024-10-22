# -*- coding: utf-8 -*-
from sys import stdin


def div2(lst):
    _l = len(lst)
    if _l <= 3:
        return lst[0]*lst[1]
    else:
        _h = _l//2
        if _l % 2 == 1:
            _h += 1
        return div2(lst[:_h]) + div2(lst[_h:])


if __name__ == "__main__":
    _n = int(stdin.readline())
    _lst = [i for i in range(1, _n+1)]

    ans = div2(_lst)
    print(ans)
