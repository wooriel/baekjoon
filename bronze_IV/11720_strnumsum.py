#-*- coding: utf-8 -*-

def strsum(length, s):
    sum = 0
    for i in range(length):
        sum += int(s[i])

    return sum

if __name__ == "__main__":
    n = int(input())
    string = input()

    print(strsum(n, string))