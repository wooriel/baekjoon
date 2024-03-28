# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    items, word = stdin.readline().rstrip().split()
    items = int(items)

    sum = 0
    for i in range(items):
        name, num = stdin.readline().rstrip().split()
        lstname = name.split("_")
        num = int(num)
        scontain = False
        for elem in lstname:
            if elem == word:
                scontain = True
                break
        if scontain:
            sum += num

    print(sum)