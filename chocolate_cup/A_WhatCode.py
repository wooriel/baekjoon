# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    line = stdin.readline().rstrip()
    if line[0] == "\"" and line[-1] == "\"":
        alph = False
        for i in range(1, len(line) - 1):
            if line[i].isalpha():
                alph = True
                break
        if alph:
            print(line[1:-1])
        else:
            print("CE")
    else:
        print("CE")