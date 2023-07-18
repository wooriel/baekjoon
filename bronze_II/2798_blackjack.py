# -*- coding: utf-8 -*-
import itertools

if __name__ == "__main__":
    n, max_num = map(int, input().split())

    lst = list(map(int, input().split()))

    subsets = itertools.permutations(lst, 3)

    sums = set()
    for subset in subsets:
        sums.add(sum(subset)) # subset[0]+subset[1]+subset[2]

    sums = list(sums)
    sums.sort() # not needed
    to_print = 0
    for i in range(len(sums)):
        if max_num > sums[i]:
            if i == len(sums) - 1:
                to_print = sums[i]
        elif max_num == sums[i]:
            to_print = sums[i]
        else: # max_num < sums[i]
            to_print = sums[i-1]
            break

    print(to_print)