#-*- coding: utf-8 -*-

def dan_printer(n):
    for i in range(9):
        print("{} * {} = {}".format(n, i+1, n*(i+1)))

if __name__ == "__main__":
    n = int(input())

    dan_printer(n)