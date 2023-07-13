# -*- coding: utf-8 -*-

if __name__ == "__main__":
    length = int(input())
    s = input().upper()
    R = 31
    M = 1234567891

    sum = 0
    for i in range(length):
        a_i = ord(s[i]) - ord('A') + 1
        sum += a_i * pow(R, i)

    print(sum % M)

