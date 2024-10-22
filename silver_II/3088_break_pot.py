# -*- coding: utf-8 -*-
from sys import stdin


def _compare(lst1, lst2):
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i] == lst2[j]:
                return True
    else:
        return False


if __name__ == "__main__":
    n = int(stdin.readline())

    lst = list(map(int, stdin.readline().split()))
    pool = set(lst)
    cnt = 1
    for i in range(1, n):
        lst = list(map(int, stdin.readline().split()))
        _insert = True
        for j in range(len(lst)):
            if lst[j] in pool:
                pool.update(set(lst))  # 깨지더라도 업데이트 되는게 중요
                _insert = False
                break
        if _insert:
            pool.update(set(lst))
            cnt += 1

    print(cnt)
    # cnt = 0
    # while len(_map) >= 1:
    #     rem_idx = set()
    #     rem_idx.add(0)
    #     for i in range(1, len(_map)):
    #         if _compare(_map[0], _map[i]):
    #             rem_idx.add(i)

    #     to_rem = list(rem_idx)
    #     to_rem.sort(reverse=True)
    #     for elem in to_rem:
    #         del _map[elem]
    #     cnt += 1

    # print(cnt)
