# -*- coding:utf-8 -*-

if __name__ == "__main__":
    length = int(input())
    a = map(int, input().split())
    b = map(int, input().split())
    a = sorted(a)
    b = sorted(b)
    
    sum = 0
    for i in range(length):
        sum += a[i] * b[length - i - 1]

    print(sum)