# -*- coding: utf-8 -*-
from sys import stdin

def insert_pos(lst, numtoadd):
    if len(lst) == 0:
        return 0
    else:
        s, e = 0, len(lst)
        while s < e:
            half = (s + e) // 2
            if lst[half] == numtoadd:
                return half + 1
            elif lst[half] <= numtoadd:
                s = half + 1
            else:
                e = half - 1
        if s == len(lst) or numtoadd < lst[s]:
            return s
        else:
            return s + 1
        
# 일반적인 이진으로 풀었더니 시간초과 뜸
if __name__ == "__main__":
    cases = int(stdin.readline())

    for i in range(cases):
        num_op = int(stdin.readline())
        queue = []
        for j in range(num_op):
            op, num = stdin.readline().split()
            num = int(num)
            if op == 'I':
                idx = insert_pos(queue, num)
                queue.insert(idx, num)
            else: # op == 'D'
                if len(queue) != 0:
                    if num == -1:
                        del queue[0]
                    else: # num == 1
                        queue.pop()
        if len(queue) == 0:
            print("EMPTY")
        else:
            print("{} {}".format(queue[-1], queue[0]))