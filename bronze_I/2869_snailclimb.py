# -*- coding: utf-8 -*-
import math

if __name__ == "__main__":
    up, down, length = map(int, input().split())

    res = math.ceil((length - up) / (up-down)) + 1
    print(res)