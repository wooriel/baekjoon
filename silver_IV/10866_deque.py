# -*- coding: utf-8 -*-
# from collections import deque

class Deque:
    lst = []

    # 공통적으로 있는 부분을 없앨 수 있지 않을까
    # if len(self.lst) == 0:
    #     return -1

    def push_front(self, i:int):
        self.lst.insert(0, i)

    def push_back(self, i:int):
        self.lst.append(i)

    def pop_back(self):
        if len(self.lst) == 0:
            return -1
        else:
            return self.lst.pop(-1)
        
    def pop_front(self):
        if len(self.lst) == 0:
            return -1
        else:
            return self.lst.pop(0)
        
    def size(self):
        return len(self.lst)
    
    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0
        
    def front(self):
        if len(self.lst) == 0:
            return -1
        else:
            return self.lst[0]
    
    def back(self):
        if len(self.lst) == 0:
            return -1
        else:
            return self.lst[-1]

if __name__ == "__main__":
    n = int(input())
    d = Deque()
    res = list()

    for i in range(n):
        lst = input().split()
        cmd = lst[0]
        if len(lst) == 2:
            if cmd == "push_front":
                d.push_front(int(lst[1]))
            else: # cmd == "push_back"
                d.push_back(int(lst[1]))
        else:
            if cmd == "pop_front":
                res.append(d.pop_front())
            elif cmd == "pop_back":
                res.append(d.pop_back())
            elif cmd == "size":
                res.append(d.size())
            elif cmd == "empty":
                res.append(d.empty())
            elif cmd == "front":
                res.append(d.front())
            else: # cmd == "back"
                res.append(d.back())

    for r in res:
        print(r)