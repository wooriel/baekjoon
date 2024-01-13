# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    n = int(input())

    res = []
    for i in range(n):
        word = stdin.readline().rstrip()
        s = word[0]
        e = word[0]
        count = 0
        while True:
            try:
                e = word[count]
                count += 1
            except IndexError:
                break

        res.append("{}{}".format(s, e))

    for elem in res:
        print(elem)