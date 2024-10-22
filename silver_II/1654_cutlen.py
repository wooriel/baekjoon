# -*- coding: utf-8 -*-

def works(lst:int, k, n):
    rope_num = 0
    for knot in lst:
        rope_num += knot//k

    if rope_num >= n:
        return 1
    else:
        return 0


def find_maxlen(lst, lim, n):
    start = 1
    end = lim

    prev_k = 0
    while start != end:
        k = (start + end)//2
        if prev_k == k:
            break
        if works(lst, k, n):
            start = k
        else:
            end = k - 1
        prev_k = k

    if works(lst, end, n):
        return end
    else:
        return start


if __name__ == "__main__":
    k, n = map(int, input().split())

    lens = []
    sum = 0
    for i in range(k):
        lens.append(int(input()))
        sum += lens[-1]

    limit = sum // n

    ans = find_maxlen(lens, limit, n)
    print(ans)