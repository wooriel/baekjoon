# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    while True:
        s1, s2, s3 = map(int, stdin.readline().split())
        if s1 == 0 and s2 == 0 and s3 == 0:
            break
        if s1 + s2 <= s3 or s2 + s3 <= s1 or s3 + s1 <= s2:
            print("Invalid")
        else:
            if s1 == s2 and s2 == s3 and s3 == s1:
                print("Equilateral")
            elif s1 == s2 or s2 == s3 or s3 == s1:
                print("Isosceles")
            else:
                print("Scalene")
