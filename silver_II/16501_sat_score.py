# -*- coding: utf-8 -*-
from sys import stdin
from itertools import combinations
from copy import deepcopy
from collections import defaultdict

if __name__ == "__main__":
    lst = list(map(int, stdin.readline().split()))
    lst.sort()
    idx_lst = [i for i in range(0, 8)]
    comb_lst = list(combinations(idx_lst, 4))

    comb_lst = set(comb_lst)
    res = defaultdict(set)
    for elem in comb_lst:
        diff = lst[elem[0]] + lst[elem[3]] - lst[elem[1]] - lst[elem[2]]
        if diff > 0:
            val = (20 - diff) / 20.
        else:
            val = (20 + diff) / 20.
        for i in range(len(elem)):
            res[val].add(elem[i])  # 이걸 나중에 값마다 값-index(set)으로 만들어서 한번에 없애기

    # res.sort(key=lambda x: x[0])
    cur_min = 1.0
    lst2 = deepcopy(lst)
    _keys = list(res.keys())
    _keys.sort()
    while len(lst2) > 0 and len(_keys) > 0:  # 사실 res 리스트가 비게 될 경우는 없음
        cur_min = _keys.pop()
        elem = res[cur_min]
        for idx in elem:
            cur = lst[idx]
            try:
                lst2.remove(cur)
            except:
                pass

    # print(cur_min)
    _str = "{:.2f}".format(cur_min)
    if len(_str) <= len(str(cur_min)):
        print(_str)
    else:
        print("{:.1f}".format(cur_min))
