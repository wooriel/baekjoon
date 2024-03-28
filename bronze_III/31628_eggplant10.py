# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    flag = 0
    field = []
    for i in range(10):
        lst = list(stdin.readline().split())
        felem = lst[0]
        if flag != 1:
            for j in range(1, len(lst)):
                if felem == lst[j]:
                    if j == len(lst) - 1:
                        flag = True
                else:
                    break
        field.append(lst)

    if flag:
        print(1)
    else:
        # check vertical
        cur = 1
        for i in range(0, 10):
            felem = field[0][i]
            while cur < len(field):
                if felem != field[cur][i]:
                    break
                cur += 1
            if cur == len(field):
                flag = 1
                break
            cur = 0
        if flag:
            print(1)
        else:
            print(0)