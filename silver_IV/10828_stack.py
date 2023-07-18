# -*- coding: utf-8 -*-

from collections import deque

if __name__ == "__main__":
    n = int(input())


    s = deque()
    lst = []
    for i in range(n):
        lst_cmd = input().split()
        if len(lst_cmd) == 2:
            s.append(int(lst_cmd[1]))
        else:
            cmd = lst_cmd[0]
            if len(list(s)) == 0:
                to_print = -1
                if cmd == 'empty':
                    to_print = 1
                elif cmd == 'size':
                    to_print = 0
            else:
                if cmd == 'pop':
                    to_print = s.pop()
                elif cmd == 'size':
                    to_print = len(list(s))
                elif cmd == 'empty':
                    to_print = 0
                else: #cmd = 'top'
                    to_print = s.pop()
                    s.append(to_print)
            lst.append(to_print)

    for elem in lst:
        print(elem)
            