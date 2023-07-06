# -*- coding: utf-8 -*-

if __name__ == "__main__":
    res = []

    a = -1
    b = -1
    while a != 0 or b != 0:
        a, b = map(int, input().split())
        res.append(a+b)

    for i in range(len(res) - 1):
        print(res[i])