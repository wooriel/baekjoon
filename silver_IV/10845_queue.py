# -*- coding: utf-8 -*-

from collections import deque

if __name__ == "__main__":
    n = int(input())

    q = deque()
    res = []
    for i in range(n):
        lst_cmd = input().split()
        if len(lst_cmd) == 2:
            q.append(int(lst_cmd[1]))
        else:
            cmd = lst_cmd[0]
            if len(list(q)) == 0:
                to_print = -1
                if cmd == 'empty':
                    to_print = 1
                elif cmd == 'size':
                    to_print = 0
            else:
                if cmd == 'pop':
                    to_print = q.popleft()
                elif cmd == 'size':
                    to_print = len(list(q))
                elif cmd == 'empty':
                    to_print = 0
                elif cmd == 'front':
                    to_print = q.popleft()
                    q.appendleft(to_print)
                else: # cmd == 'back'
                    to_print = q.pop()
                    q.append(to_print)
            res.append(to_print)

    for r in res:
        print(r)