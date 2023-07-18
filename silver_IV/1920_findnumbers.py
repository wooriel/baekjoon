# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n = int(input())

    orig = set(map(int, input().split()))

    m = int(input())

    to_find = list(map(int, input().split()))

    for elem in to_find:
        if elem in orig:
            print(1)
        else:
            print(0)