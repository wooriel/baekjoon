# -*- coding: utf-8 -*-
from sys import stdin


def ret_word(_str, cond="upper"):
    _word = []
    last_idx = -1
    if cond == "upper":
        for i in range(1, len(_str)):
            if _str[i].isupper():
                if last_idx == -1:
                    _word.append(_str[:i].lower())
                else:
                    _word.append(_str[last_idx:i].lower())
                last_idx = i
        if last_idx != -1:
            _word.append(_str[last_idx:].lower())
        else:  # one word
            _word.append(_str.lower())
    else:
        _word = _str.split("_")
    return _word


def print_camel(_lst):
    _l = len(_lst)
    if _l > 1:
        print("{}".format(_lst[0]), end="")
    else:
        print("{}".format(_lst[0]))
    for i in range(1, _l):
        if i != _l-1:
            print("{}{}".format(_lst[i][0].upper(), _lst[i][1:]), end="")
        else:
            print("{}{}".format(_lst[i][0].upper(), _lst[i][1:]))


def print_pascal(_lst):
    _l = len(_lst)
    for i in range(_l):
        if i != _l-1:
            print("{}{}".format(_lst[i][0].upper(), _lst[i][1:]), end="")
        else:
            print("{}{}".format(_lst[i][0].upper(), _lst[i][1:]))


if __name__ == "__main__":
    _n, var_name = stdin.readline().rstrip().split()
    _n = int(_n)

    if _n == 1 or _n == 3:  # camel case, _idx points to uppercase
        _w = ret_word(var_name)
        _wl = len(_w)
        print_camel(_w)
        print("_".join(_w))  # snake_case
        print_pascal(_w)
    else:  # n == 2
        _w = ret_word(var_name, "under")
        _wl = len(_w)
        print_camel(_w)
        print(var_name)
        print_pascal(_w)
