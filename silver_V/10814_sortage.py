# -*- coding: utf-8 -*-
# from operator import attrgetter

if __name__ == "__main__":
    n = int(input())

    lst = []
    for i in range(n):
        age, name = input().split()
        lst.append(tuple([int(age), name, i]))

    lst.sort(key = lambda elem: elem[2])
    lst.sort(key = lambda elem: elem[0])
    # lst.sort(key = attrgetter(2))
    # lst.sort(key = attrgetter(0))

    for i in range(n):
        print("{} {}".format(lst[i][0], lst[i][1]))