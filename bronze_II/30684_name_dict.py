# -*- coding: utf-8 -*-
from sys import stdin


if __name__ == "__main__":
    n = int(stdin.readline())

    _min = "ZZZZZ"
    for i in range(n):
        _cur = stdin.readline().rstrip()
        if len(_cur) != 3:
            continue
        else:
            if _min > _cur:
                _min = _cur

    print(_min)
