# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict


if __name__ == "__main__":
    _str = stdin.readline().rstrip()

    char_dict = defaultdict(int)
    for i in range(len(_str)):
        char_dict[_str[i]] += 1

    _key = list(char_dict.keys())
    _key.sort()

    _odd = 0
    lst = []
    flag = -1
    _odd_alp = ""
    for elem in _key:
        _cur = char_dict[elem]
        if _cur % 2 == 1:
            _odd += 1
            if _odd > 1:
                print("I'm Sorry Hansoo")
                break
            else:
                _odd_alp = elem
                for i in range(_cur//2):
                    lst.append(elem)
                else:
                    flag = 1
        else:
            for i in range(_cur//2):
                lst.append(elem)

    ans = []
    if _odd <= 1:
        ans.extend(lst)
        ans.append(_odd_alp)
        lst.reverse()
        ans.extend(lst)
        print("".join(ans))
