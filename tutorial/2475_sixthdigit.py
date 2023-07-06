# -*- coding: utf-8 -*-

if __name__ == "__main__":
    digits = list(map(int, input().split()))

    sqsum = 0
    for i in range(len(digits)):
        sqsum += pow(digits[i], 2)

    print(sqsum % 10)