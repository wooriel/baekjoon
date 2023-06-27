# -*- coding:utf-8 -*-

def divide_one(n, ns, len, num=1):
    if n + ns / 2 > len:
        return divide_one(n, ns/2, len, num)
    else:
        if n + ns / 2 == float(len):
            return num
        else:
            n += ns / 2
            num += 1
            return divide_one(n, ns/2, len, num)

if __name__ == "__main__":
    length = int(input())
    stick = 64
    if length == stick:
        print(1)
    else:
        print(divide_one(0, stick, length, 1))
