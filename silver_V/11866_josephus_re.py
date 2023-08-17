# -*- coding: utf-8 -*-

# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

if __name__ == "__main__":
    n, k = map(int, input().split())

    lst = [i for i in range(1, n+1)]
    res = []

    idx = -1
    while len(lst) != 0:
        idx += k
        if idx >= len(lst):
            idx %= len(lst)
        res.append(str(lst[idx]))
        del lst[idx]
        idx -= 1

    print("<{}>".format(", ".join(res)))