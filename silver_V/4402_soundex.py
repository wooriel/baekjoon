# -*- coding: utf-8 -*-
from sys import stdin


def get_sound(_str):
    soundex = []
    prev = '-1'
    for i in range(len(_str)):
        num = '0'
        if _str[i] in {'B', 'F', 'P', 'V'}:
            num = '1'
        elif _str[i] in {'C', 'G', 'J', 'K', 'Q', 'S', 'X', 'Z'}:
            num = '2'
        elif _str[i] in {'D', 'T'}:
            num = '3'
        elif _str[i] == 'L':
            num = '4'
        elif _str[i] in {'M', 'N'}:
            num = '5'
        elif _str[i] == 'R':
            num = '6'
        # else:
        #     continue
        if prev == -1 or (prev != num and num != '0'):
            soundex.append(num)
        prev = num
    ans = ''.join(soundex)
    return ans


if __name__ == "__main__":
    while True:
        s = stdin.readline().rstrip()
        if s == '':
            break
        else:
            p = get_sound(s)
            print(p)
