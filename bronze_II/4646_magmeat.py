# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    while True:
        lst = list(map(int, stdin.readline().split()))

        n = lst[0]
        if n == 0:
            break
        else:
            left = 0
            total = sum(lst) - lst[0]
            for i in range(1, n+1):
                left += lst[i]
                if left == total - left:
                    print(
                        "Sam stops at position {} and Ella stops at position {}.".format(i, i+1))
                    break
            if left == total:
                print("No equal partitioning.")
