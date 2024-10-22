# -*- coding: utf-8 -*-
from sys import stdin


def check_four(_m, r_c, idx):
    _l = len(_m[idx])
    if r_c == 'r':
        first = _m[idx][0]
        for i in range(1, _l):
            if first != _m[idx][i]:
                return False
        return True
    else:  # r_c == 'c'
        first = _m[0][idx]
        for i in range(1, _l):
            if first != _m[i][idx]:
                return False
        return True


def check_modified_line(_m, r_c, ridx, cidx):
    _l = len(_m[0])
    _str = []
    if r_c == 'r':
        str1 = []  # add row (change cidx)
        if cidx != 0:  # value cidx is at most len-2
            str1.extend(_m[ridx][:cidx])
        str1.extend(_m[ridx][cidx+1:cidx+2])
        str1.extend(_m[ridx][cidx:cidx+1])
        if cidx != _l-1:
            str1.extend(_m[ridx][cidx+2:])
        _str.append(''.join(str1))

        str2 = []  # add first column
        if ridx != 0:
            for i in range(ridx):
                str2.append(_m[i][cidx])
        str2.extend(_m[ridx][cidx+1:cidx+2])
        if ridx != _l-1:
            for i in range(ridx+1, _l):
                str2.append(_m[i][cidx])
        _str.append(''.join(str2))

        str3 = []
        if ridx != 0:
            for i in range(ridx):
                str3.append(_m[i][cidx+1])
        str3.extend(_m[ridx][cidx:cidx+1])
        if ridx != _l-1:
            for i in range(ridx+1, _l):
                str3.append(_m[i][cidx+1])
        _str.append(''.join(str3))

    else:  # r_c == 'c'
        str1 = []  # wrong
        if ridx != 0:
            for i in range(ridx):
                str1.append(_m[i][cidx])
            # str1.extend(_m[:ridx][cidx])
        str1.append(_m[ridx+1][cidx])
        str1.append(_m[ridx][cidx])
        if ridx != _l-1:
            for i in range(ridx+2, _l):
                str1.append(_m[i][cidx])
            # str1.extend(_m[ridx+2:][cidx])
        _str.append(''.join(str1))

        # str1 = []  # add row (change cidx)
        # if cidx != 0:  # value cidx is at most len-2
        #     str1.extend(_m[ridx][:cidx])
        # str1.extend(_m[ridx][cidx+1:cidx+2])
        # str1.extend(_m[ridx][cidx:cidx+1])
        # if cidx != _l-1:
        #     str1.extend(_m[ridx][cidx+2:])
        # _str.append(''.join(str1))

        str2 = []
        if cidx != 0:
            str2.extend(_m[ridx][:cidx])
        str2.extend(_m[ridx+1][cidx:cidx+1])
        if cidx != _l-1:
            str2.extend(_m[ridx][cidx+1:])
        _str.append(''.join(str2))

        str3 = []
        if cidx != 0:
            str3.extend(_m[ridx+1][:cidx])
        str3.extend(_m[ridx][cidx:cidx+1])
        if cidx != _l-1:
            str3.extend(_m[ridx+1][cidx+1:])
        _str.append(''.join(str3))

    return _str


def count_candy(_str):  # array of three strings
    _l_lst = len(_str)  # 3
    _l_str = len(_str[0])  # length of string
    max_len = 0
    prev = -1
    for j in range(_l_lst):
        _len = []
        _cl = 0
        for i in range(_l_str):
            cur = _str[j][i]
            if prev == -1 or prev == cur:
                _cl += 1
                if i == _l_str-1:
                    _len.append(_cl)
            else:
                _len.append(_cl)
                _cl = 1
            prev = cur
        cur_len = max(_len)
        if cur_len == _l_str:
            return _l_str
        if max_len < cur_len:
            max_len = cur_len

    return max_len


if __name__ == "__main__":
    _map = []

    dim = int(stdin.readline())
    for i in range(dim):
        _str = stdin.readline().rstrip()
        _map.append(_str)

    flag = False
    for i in range(dim):
        flag |= check_four(_map, 'r', i)
        flag |= check_four(_map, 'c', i)
        if flag:
            print(dim)
            break

    if flag == False:
        # brute-force
        # _s = check_modified_line(_map, 'r', 0, 0)
        # _s2 = check_modified_line(_map, 'c', 0, 0)

        # print(_s)
        # print(_s2)
        r_max = 0
        c_max = 0
        for i in range(dim):
            for j in range(dim):
                r_cur, c_cur = 0, 0
                if i < dim-1:
                    c_str = check_modified_line(_map, 'c', i, j)
                    # find n of longest string, and if it match with dim, terminate
                    c_cur = count_candy(c_str)
                if j < dim-1:
                    r_str = check_modified_line(_map, 'r', i, j)
                    r_cur = count_candy(r_str)
                if r_cur > r_max:
                    r_max = r_cur
                if c_cur > c_max:
                    c_max = c_cur
                if r_cur == dim or c_cur == dim:
                    break

        print(max(r_max, c_max))
