# -*- coding: utf-8 -*-
from sys import stdin
import copy

if __name__ == "__main__":
    _n = int(stdin.readline())
    _word1 = list(map(int, stdin.readline().split()))
    # _word1 = list(stdin.readline().split()) # for string input
    _m = int(stdin.readline())
    _word2 = list(map(int, stdin.readline().split()))
    # _word2 = list(stdin.readline().split())

    _map = []
    for i in range(_n+1):
        _lst = [[] for k in range(_m+1)]
        _map.append(_lst)

    for i in range(1, _n+1):
        for j in range(1, _m+1):
            if _word1[i-1] == _word2[j-1]:
                _map[i][j] = copy.deepcopy(_map[i-1][j-1])
                # cut the word smaller than added character
                _idx = -1
                for k in range(len(_map[i][j])):
                    if _map[i][j][k] < _word1[i-1]:
                        # _map[i][j].insert(_word1[i-1], k)
                        _idx = k
                        break  # 이거 추가 안하면 수가 밀림
                if _idx != -1:
                    _map[i][j] = _map[i][j][:_idx]
                _map[i][j].append(_word1[i-1])
            else:
                if _map[i-1][j] > _map[i][j-1]:
                    _map[i][j] = copy.deepcopy(_map[i-1][j])
                else:
                    _map[i][j] = copy.deepcopy(_map[i][j-1])

    _len = len(_map[-1][-1])
    _lst = _map[-1][-1]
    print(_len)
    # print(" ".join(_lst))

    if _len > 0:
        # when element are numbers
        for i in range(_len):
            if i < _len - 1:
                print(_lst[i], end=" ")
            else:
                print(_lst[i])

# Test case
# 6
# 5 4 3 1 5 3
# 7
# 5 2 1 3 5 4 3
# ans: 5 5 3

# 5
# 4 4 3 3 4
# 5
# 4 3 3 4 4
# ans: 4 4 4

# 9
# 5 4 3 1 5 3 7 5 5
# 8
# 5 7 2 1 3 5 4 3
# ans: 7 5
