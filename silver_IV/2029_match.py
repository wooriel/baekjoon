# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    match = [0 for i in range(24)]
    a = 0
    idx = 0
    for i in range(10):
        if i % 3 == 0:
            lst = stdin.readline().rstrip().split('+')
            for elem in lst[1:4]:
                if elem == '--':
                    match[idx] = 1
                    a += 1
                idx += 1
        elif i % 3 == 1:
            _str = stdin.readline().rstrip()
            for i in range(0, 12, 3):
                if _str[i] == '|':
                    match[idx] = 1
                    a += 1
                idx += 1
        else:
            _str = stdin.readline().rstrip()

    # sm = ''.join(match)
    a = 24-a
    b = 0
    _idx = [0, 1, 2, 7, 8, 9, 14, 15, 16]
    for i in _idx:
        if match[i] and match[i+3] and match[i+4] and match[i+7]:
            b += 1

    _idx2 = [0, 1, 7, 8]
    for i in _idx2:
        if match[i] and match[i+1] and match[i+3] and match[i+5] and match[i+10] and match[i+12] and match[i+14] and match[i+15]:
            b += 1

    if match[0] and match[1] and match[2] and match[3] and match[6] and match[10] and match[13] and match[17] and match[20] and match[21] and match[22] and match[23]:
        b += 1

    print('{} {}'.format(a, b))
