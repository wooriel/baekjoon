# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    a, b, c = map(int, stdin.readline().split())

    # mul = 1
    # if b % 2 == 1:
    #     mul *= a
    #     if mul > c:
    #         mul %= c

    # print(mul)

    def mul(time, val):
        if time == 1:
            return val % c
        else:
            if time % 2 == 0:
                _v = mul(time//2, pow(val, 2, c))
                _ret = pow(_v, 2, c)
            else:  # time % 2 == 1:
                _v = mul(time//2, pow(val, 2, c))
                _v_1 = mul(time//2, pow(val, 2, c) * pow(val, 1, c))
                _ret = _v * _v_1
            return _ret

    print(mul(b, a % c))

    # val = a
    # while b > 1:
    #     if b % 2 == 1:
    #         val = val * val % c * val % c
    #     else:
    #         val = val % c * val % c
    #     b = b//2

    # print(val % c)
