# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    num_ppl = int(stdin.readline().rstrip())
    lst = list(map(int, stdin.readline().rstrip().split()))

    lst.sort()
    sum = 0
    for i in range(num_ppl):
        sum += lst[i] * (num_ppl - i)

    print(sum)