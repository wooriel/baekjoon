# -*- coding: utf-8 -*-

# memory issue (sort by reference and index later)

def merge_sort(lst):
    if len(lst) == 1:
        return lst
    elif len(lst) == 2:
        return merge(lst[:1], lst[1:])
    else:
        half = n//2
        l = merge_sort(lst[:half])
        r = merge_sort(lst[half:])
        return merge(l, r)
    

def merge(l, r):
    lidx = 0
    ridx = 0
    merged = []
    while lidx != len(l) and ridx != len(r):
        if l[lidx] <= r[ridx]:
            merged.append(l[lidx])
            lidx += 1
        else:
            merged.append(r[ridx])
            ridx += 1

    if lidx == len(l):
        merged.extend(r[ridx:])
    if ridx == len(r):
        merged.extend(l[lidx:])

    return merged

if __name__ == "__main__":
    n = int(input())

    lst = []
    for i in range(n):
        lst.append(int(input()))

    sorted = merge_sort(lst)

    for elem in sorted:
        print(elem)    