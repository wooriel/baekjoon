# -*- coding: utf-8 -*-
from sys import stdin


def inner(_lst):
    # _fir = {'(', ')'}
    _sec = {'*', '/'}
    _thr = {'+', '-'}

    if len(_lst) < 3:
        _ret = "".join(_lst)
        return _ret
    elif len(_lst) == 3:
        _ret = "".join([_lst[0], _lst[2], _lst[1]])
        return _ret
    else:
        _s, _e = 0, -1
        while _s != -1:  # parenthesis
            _s = -1
            for i in range(len(_lst)):
                if _lst[i] == '(':
                    _s = i+1
                    for j in range(i+1, len(_lst)):
                        if _lst[j] == '(':
                            _s = j+1
                        elif _lst[j] == ')':
                            _e = j  # last parenthesis
                            break
                    break
            if _s != -1:
                n_val = inner(_lst[_s:_e])
                del _lst[_s-1:_e+1]
                _lst.insert(_s-1, n_val)

        _s2 = 0
        while _s2 != -1:
            _s2 = -1
            for k in range(len(_lst)):
                if _lst[k] in _sec:
                    _s2 = k-1
                    break
            if _s2 != -1:
                n_val = inner(_lst[_s2:_s2+3])
                del _lst[_s2:_s2+3]
                _lst.insert(_s2, n_val)

        _s3 = 0
        while _s3 != -1:
            _s3 = -1
            for m in range(len(_lst)):
                if _lst[m] in _thr:
                    _s3 = m-1
                    break
            if _s3 != -1:
                n_val = inner(_lst[_s3:_s3+3])
                del _lst[_s3:_s3+3]
                _lst.insert(_s3, n_val)

        return _lst[0]


if __name__ == "__main__":
    _str = stdin.readline().rstrip()

    _lst = []
    n = len(_str)
    for i in range(n):
        _lst.append(_str[i])

    ans = inner(_lst).rstrip()
    print(ans)
