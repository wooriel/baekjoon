# -*- coding: utf-8 -*-
from sys import stdin
from itertools import combinations

if __name__ == "__main__":
    case = int(stdin.readline())
    for j in range(case):
        n, p = map(int, stdin.readline().split())
        lst = list(map(int, stdin.readline().split()))

        rem = []  # stores remainder of the group
        count = 0
        for elem in lst:
            _rem = elem % p
            if _rem == 0:  # if no remainder, give chocolate first
                count += 1
            else:
                rem.append(_rem)

        rem.sort()

        _l = len(rem)
        if _l == 0:
            continue
        elif len(rem) == 1:
            count += 1
        else:
            if p == 2:
                # [1, 1] one case
                to_add = _l//2
                count += to_add
                if _l % 2 == 1:
                    count += 1
            else:
                if p == 3:
                    _rem_lst = [[1, 2], [1, 1, 1]]
                else:  # p == 4
                    _rem_lst = [[1, 3], [2, 2], [1, 1, 2], [1, 1, 1, 1]]

                to_delete_idx = []
                if _l < p:
                    for i in range(len(_rem_lst)):
                        cur = _rem_lst[i]
                        if len(cur) < _l:
                            to_delete_idx.append(i)
                for elem in to_delete_idx:
                    del _rem_lst[elem]

                for elem in _rem_lst:
                    to_delete = []
                    if len(elem) > len(rem):
                        break
                    else:
                        for i in range(len(elem)):
                            findee_cur = elem[i]
                            finder_cur = rem[0]
                            # 없을때까지 찾아야함
                            finder_idx = 0
                            while finder_idx != -1:
                                finder_idx = -1
                                for j in range(len(rem)):
                                    finder_cur = rem[j]
                                    if findee_cur == finder_cur:
                                        finder_idx = j
                                        break
                                    if finder_idx != -1:
                                        to_delete.append(finder_idx)
                                    else:
                                        break
                                to_delete.reverse()
                                for elem in to_delete:
                                    del rem[elem]

                if len(rem) > 0:
                    count += 1

        print("Case #{}: {}".format(j+1, count))
