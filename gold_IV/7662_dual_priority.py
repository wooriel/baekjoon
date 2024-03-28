# -*- coding: utf-8 -*-
from sys import stdin
# from collections import deque
# from collections import defaultdict


# 사실 이렇게 풀면 안됨
if __name__ == "__main__":
    cases = int(stdin.readline())
    for i in range(cases):
        operations = int(stdin.readline())
        # lst = deque()
        lst = {}
        for j in range(operations):
            op, num = map(str, stdin.readline().split())
            num = int(num)
            if op == 'I':
                if num not in lst:
                    lst[num] = 1
                else:
                    lst[num] += 1
                # if len(lst) == 0:
                #     lst.append(num)
                # else:
                #     lst[num] += 1
                    # binary search and input (insert O(n))
                    # start, end = 0, len(lst)
                    # if lst[start] >= num:
                    #     lst.appendleft(num)
                    # elif lst[-1] <= num:
                    #     lst.append(num)
                    # else:
                    #     while True:
                    #         half = (start+end)//2
                    #         melem = lst[half]
                    #         if half == start:
                    #             if num < melem:
                    #                 lst.insert(half, num)
                    #             else:
                    #                 lst.insert(half+1, num)
                    #             break
                    #         elif melem > num:
                    #             end = half
                    #         else:
                    #             start = half
            else:
                if len(lst) == 0:
                    continue
                else:
                    key = list(lst.keys())
                    if num == -1:
                        # lst.popleft()
                        _min = min(key)
                        lst[_min] -= 1
                        if lst[_min] == 0:
                            del lst[_min]
                    else:
                        # lst.pop()
                        _max = max(key)
                        lst[_max] -= 1
                        if lst[_max] == 0:
                            del lst[_max]

        if len(lst) == 0:
            print('EMPTY')
        else:
            key = list(lst.keys())
            # print("{} {}".format(lst[-1], lst[0]))
            print("{} {}".format(max(key), min(key)))