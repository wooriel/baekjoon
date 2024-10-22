# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict


if __name__ == '__main__':
    k = int(stdin.readline())
    _str = stdin.readline().rstrip()

    def get_dist(end, _dict: dict):
        if len(list(_dict.keys())) == 0:
            for j in range(end-k, end):
                cur = _str[j]
                _dict[cur] += 1
        else:
            _dict[_str[end-k-1]] -= 1
            if _dict[_str[end-k-1]] == 0:
                del _dict[_str[end-k-1]]
            _dict[_str[end-1]] += 1

        _ord = list(_dict.keys())
        _ord.sort()

        max_occ = 0
        max_alp = 'a'
        for elem in _ord:
            cur_occ = _dict[elem]
            if max_occ < cur_occ:
                max_occ = cur_occ
                max_alp = elem

        dist = ord(max_alp) - ord('a') + 1

        return dist, _dict

    res = []
    res.append(_str[:k])
    occurence = defaultdict(int)
    for i in range(k, len(_str)):
        prev = _str[i]
        dist, occurence = get_dist(i, occurence)
        cur = chr((ord(prev) - ord('a') + dist) % 26 + ord('a'))
        res.append(cur)

    print(''.join(res))
