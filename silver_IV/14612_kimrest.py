# -*- coding: utf-8 -*-
from sys import stdin


def print_lst(lst):
    if len(lst) == 0:
        print('sleep')
    else:
        for k in range(len(lst)):
            if k == len(lst)-1:
                print(lst[k][0])
            else:
                print(lst[k][0], end=' ')
    return


if __name__ == "__main__":
    n, m = map(int, stdin.readline().split())

    order = []
    for i in range(n):
        lst = list(stdin.readline().rstrip().split())
        if len(lst) > 1:
            if lst[0] == 'order':
                tab = int(lst[1])
                t = int(lst[2])
                order.append((tab, t))
            else:
                t = int(lst[1])
                idx = 0
                for j in range(len(order)):
                    if order[j][0] == t:
                        idx = j
                        break
                del order[idx]
        else:
            order.sort(key=lambda x: x[0])
            order.sort(key=lambda x: x[1])
        print_lst(order)
