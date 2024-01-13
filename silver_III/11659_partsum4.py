# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    nums, test = map(int, stdin.readline().split())
    lst = list(map(int, stdin.readline().split()))
    
    sums = []
    # n위치까지의 sum을 미리 계산
    sum_upto = 0
    for i in range(nums):
        sum_upto += lst[i]
        sums.append(sum_upto)

    res = []
    for i in range(test):
        s, e = map(int, stdin.readline().split())
        if s == 1:
            res.append(sums[e-1])
        else:
            res.append(sums[e-1] - sums[s-2])
        # if e-s < nums // 2:
        #     total = 0
        #     for j in range(s-1, e):
        #         total += lst[j]
        #     res.append(total)
        # else:
        #     total = lst_sum
        #     for m in range(s-1):
        #         total -= lst[m]
        #     for n in range(e, nums):
        #         total -= lst[n]
        #     res.append(total)
        # res.append(sum(lst[s-1:e]))

    for elem in res:
        print(elem)