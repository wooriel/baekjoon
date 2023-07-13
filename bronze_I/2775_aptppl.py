# -*- coding: utf-8 -*-

def pascal_count(a, b):
    if a == 0:
        return b
    prevline = [1, 1]
    for i in range(a + b - 1):
        line = []
        line.append(prevline[0])
        for j in range(len(prevline)):
            if j == len(prevline) - 1:
                line.append(prevline[j])
            else:
                line.append(prevline[j] + prevline[j+1])
        prevline = line

    return line[b-1]

if __name__ == "__main__":
    n = int(input())

    cases = []
    for i in range(n):
        a = int(input())
        b = int(input())
        cases.append(pascal_count(a, b))

    for c in cases:
        print(c)