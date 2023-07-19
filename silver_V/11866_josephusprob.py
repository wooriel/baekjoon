# -*- coding: utf-8 -*-

class circle_queue:
    lst = []
    k = 0
    pointer = -1
    res = []

    def __init__(self, num, k):
        self.lst = [str(i) for i in range(1, num+1)]
        self.k = k

    def add_k(self):
        if self.pointer + 1 == len(self.lst):
            self.pointer = 0
        else:
            self.pointer += 1

    def cal_one_order(self):
        for i in range(self.k):
            self.add_k()
            while self.lst[self.pointer] in self.res:
                self.add_k()
        self.res.append(self.lst[self.pointer])

    def cal_all_order(self):
        for i in range(len(self.lst)):
            self.cal_one_order()

    def print_circle(self):
        print("<{}>".format(", ".join(self.res)))

if __name__ == "__main__":
    n, k = map(int, input().split())

    cq = circle_queue(n, k)
    cq.cal_all_order()
    cq.print_circle()