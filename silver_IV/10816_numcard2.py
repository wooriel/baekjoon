# -*- coding: utf-8 -*-

## does not work yet - 시간초과 떠서 수정하다가 맒

from collections import defaultdict

if __name__ == "__main__":
    n = int(input())
    
    nlst = list(map(int, input().split()))

    m = int(input())

    mlst = list(map(int, input().split()))
    # {} for k, v in iterable
    mdict = defaultdict.fromkeys(mlst, 0)

    for elem in nlst:
        try:
            mdict[elem] += 1
        except KeyError:
            continue

    for elem in mlst: # dictionary는 키 중복이 안되어서 m에서 같은 수를 두번 구하라고 할때 하나만 프린트함
        print(str(mdict[elem]), end=" ")

    # print(" ".join(str(v) for v in mdict.values()))