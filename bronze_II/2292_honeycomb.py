# -*- coding: utf-8 -*-
from sys import stdin

def count_room(n):
    level = 1
    nums = 1
    while n > nums:
        nums += level * 6
        level += 1

    return level

if __name__ == "__main__":
    n = int(stdin.readline())

    print(count_room(n))