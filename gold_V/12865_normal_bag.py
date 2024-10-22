# -*- coding: utf-8 -*-
from sys import stdin


if __name__ == "__main__":
    n, k = map(int, stdin.readline().split())

    items = []
    for i in range(n):
        w, v = map(int, stdin.readline().split())
        items.append((w, v, v/w))

    items.sort(key=lambda x: x[2], reverse=True)
    items.sort(key=lambda x: x[0])
    _map = []
    for i in range(k+1):
        bag = [set() for i in range(n+1)]
        _map.append(bag)

    for i in range(1, k+1):
        for j in range(1, n+1):
            c_i = items[j-1]  # weignt, value
            _map[i][j] = _map[i][j-1]  # same weight, previous item slot
            sum1 = 0
            for elem in _map[i][j-1]:
                sum1 += items[elem][1]
            sum2 = 0
            for elem in _map[i-1][j]:
                sum2 += items[elem][1]
            _max = max(sum1, sum2)
            if _max == sum2:
                _map[i][j] = _map[i-1][j]
            if c_i[0] <= i:
                # if c_i in _map[i-c_i[0]][j]:
                #     _map[i][j] = _map[i][j-1]
                # else:
                # sum1 = sum(_map[i][j-1])
                # for elem in _map[i][j-1]:
                #     sum1 += items[elem][1]
                # sum2 = sum(_map[i-1][j])
                # for elem in _map[i-1][j]:
                #     sum2 += items[elem][1]
                n_set = _map[i-c_i[0]][j].union({j-1})
                sum3 = 0
                for elem2 in n_set:
                    sum3 += items[elem2][1]
                if _max < sum3:
                    _map[i][j] = n_set

    ans = 0
    for elem in _map[-1][-1]:
        ans += items[elem][1]
    print(ans)
