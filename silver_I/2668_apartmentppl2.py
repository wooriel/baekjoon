# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque


if __name__ == "__main__":
    n = int(stdin.readline().rstrip())

    _map = []
    count = 0
    for i in range(n):
        lst = []
        num_str = stdin.readline().rstrip()
        prev_1 = False
        for j in range(n):
            cur_num = int(num_str[j])
            if cur_num == 1:
                if prev_1 == False:
                    prev_1 = True
                    count += 1
            lst.append(cur_num)
        _map.append(lst)