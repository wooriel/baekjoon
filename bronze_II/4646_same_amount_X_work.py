# -*- coding: utf-8 -*-
from sys import stdin


if __name__ == "__main__":
    while True:
        lst = list(map(int, stdin.readline().split()))
        n = lst[0]
        if n == 0:
            break
        else:
            s = 1
            e = n-1
            sam = lst[s]
            ella = lst[e]
            while s < e:
                if sam > ella:
                    e -= 1
                    ella += lst[e]
                elif sam < ella:
                    s += 1
                    sam += lst[s]
                else:
                    if s+1 == e:
                        print(
                            "Sam stops at position {} and Ella stops at position {}".format(s, e))
                        break
                    elif e-s == 2:
                        print("No equal partitioning.")
                        break
                    else:
                        s += 1
                        sam += lst[s]
                        e -= 1
                        ella += lst[e]
