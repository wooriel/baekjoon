# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n = int(input())
    
    res = []
    for i in range(n):
        a, b = map(int, input().split())
        res.append(a + b)

    for i in range(n):
        print(res[i])