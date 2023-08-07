# -*- coding: utf-8 -*-
from collections import deque

def can_seq(n, ans):
    d = []
    proc = []
    p = 0
    for i in range(1, n+1):
        d.append(i)
        proc.append('+')
        # pop
        while len(d) != 0 and d[-1] == ans[p]:
            d.pop()
            proc.append('-')
            p += 1

    if len(d) != 0:
        return 'NO'
    else:
        return proc


if __name__ == "__main__":
    n = int(input())

    # stack = deque([i for i in range(1, n+1)])
    ans = []
    for i in range(n):
        ans.append(int(input()))

    res = can_seq(n, ans)
    
    if res == 'NO':
        print(res)
    else:
        for r in res:
            print(r)
