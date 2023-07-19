# -*- coding: utf-8 -*-

class coord:
    x, y = 0, 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_string(self):
        print("{} {}".format(self.x, self.y))

if __name__ == "__main__":
    n = int(input())

    lst = []

    for i in range(n):
        x, y = map(int, input().split())
        lst.append(coord(x, y))

    lst.sort(key = lambda coordinate: coordinate.y)
    lst.sort(key = lambda coordinate: coordinate.x)

    for elem in lst:
        elem.print_string()