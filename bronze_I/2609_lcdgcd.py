# -*- coding: utf-8 -*-

def get_lcd(a, b):
    while a != b:
        c = abs(a-b)
        if a > b:
            if a > c:
                a = c
        else: # a < b:
            if b > c:
                b = c

    return a


def get_gcd(a, b, lcd):
    return a * b // lcd

if __name__ == "__main__":
    a, b = map(int, input().split())

    lcd = get_lcd(a, b)
    print(lcd)
    print(get_gcd(a, b, lcd))