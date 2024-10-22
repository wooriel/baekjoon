# -*- coding: utf-8 -*-
from sys import stdin


def find_winner(c, o):
    if c > o:
        return 1
    elif c < o:
        return 2
    else:
        return -1


if __name__ == "__main__":
    n = int(stdin.readline())

    city, opp = 0, 0
    tie = 1
    prev = -1
    _range = []
    s, e = 0, 0
    s_win = -1
    e_win = -1
    for i in range(n):
        t = int(stdin.readline())

        e_win = find_winner(city, opp)
        if t == 1:
            city += 1
        else:
            opp += 1
        if city == opp:
            tie += 1

        if prev != t and prev != -1:
            e = i-1
            if s_win != -1 and e_win != -1 and s_win != e_win:
                _range.append((s, e))
            s = i
            s_win = e_win
        prev = t

    e_win = find_winner(city, opp)
    if s_win != -1 and e_win != -1 and s_win != e_win:
        _range.append((s, n-1))

    _max = 0
    for elem in _range:
        cur = elem[1] - elem[0] + 1
        if _max < cur:
            _max = cur

    print("{} {}".format(city, opp))
    print(tie)
    print(_max)
