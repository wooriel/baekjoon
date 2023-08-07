# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n = int(input())
    nlst = list(map(int, input().split()))
    m = int(input())
    mlst = list(map(int, input().split()))

    res_lst = [0 for elem in range(m)]

    for i in range(n):
        try:
            idx = mlst.index(nlst[i])
            res_lst[idx] += 1
        except ValueError:
            continue

    str_res = [str(elem) for elem in res_lst]
    print(" ".join(str_res))