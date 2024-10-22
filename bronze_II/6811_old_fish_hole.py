# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    trout = int(stdin.readline())
    pike = int(stdin.readline())
    pickerel = int(stdin.readline())
    total = int(stdin.readline())

    ans = []
    max_trout = total // trout
    for i in range(max_trout+1):
        rem_pt = total - trout * i
        max_pike = rem_pt // pike
        for j in range(max_pike+1):
            rem2_pt = rem_pt - pike * j
            # if rem2_pt % pickerel == 0: does not have to be zero
            k = rem2_pt // pickerel
            ans.append((i, j, k))

    printed = set()
    printed.add((0, 0, 0))
    count = 0
    for elem in ans:
        bt, np, yp = elem
        for i in range(bt+1):
            for j in range(np+1):
                for k in range(yp+1):
                    if (i, j, k) not in printed:
                        print(
                            '{} Brown Trout, {} Northern Pike, {} Yellow Pickerel'.format(i, j, k))
                        printed.add((i, j, k))
                        count += 1
    print('Number of ways to catch fish: {}'.format(count))
