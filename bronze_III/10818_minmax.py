#-*- coding: utf-8 -*-

def find_mm(lst):
    min = lst[0]
    max = lst[0]
    for i in range(1, len(lst)):
        if min > lst[i]:
            min = lst[i]
        if max < lst[i]:
            max = lst[i]

    return min, max

if __name__ == "__main__":
    n = int(input())
    lst = list(map(int, input().split()))

    minimum, maximum = find_mm(lst)
    print("{} {}".format(minimum, maximum))