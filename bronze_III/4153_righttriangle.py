# -*- coding: utf-8 -*-

if __name__ == "__main__":
    ans = []

    lst = list(map(int, input().split()))
    while lst[0] != 0 or lst[1] != 0 or lst[2] != 0:
        lst.sort()
        if pow(lst[2], 2) == pow(lst[0], 2) + pow(lst[1], 2):
            ans.append("right")
        else:
            ans.append("wrong")
        lst = list(map(int, input().split()))

    for a in ans:
        print(a)