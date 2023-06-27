# -*- coding:utf-8 -*-

def turret(l: list[int]):
    assert len(l) == 6
    d = pow(pow(l[0]-l[3], 2) + pow(l[1]-l[4], 2), 1/2)
    base = max(l[2], l[5], d)
    sum = l[2] + l[5] + d - base
    if l[0] == l[3] and l[1] == l[4] and l[2] == l[5]:
        return -1
    if sum < base:
        return 0
    elif sum == base:
        return 1
    else: # sum > base:
        return 2

if __name__ == "__main__":
    cases = int(input())
    arr = []
    for i in range(cases):
        arr.append(list(map(int, input().split())))

    for elem in arr:
        # if 0 > elem[2] or 0 > elem[5] or 10000 < elem[2] or 10000 < elem[5]:
        #     print(-1)
        # elif -10000 > elem[0] or -10000 > elem[1] or -10000 > elem[2] or -10000 > elem[3] or 10000 < elem[0] or 10000 < elem[1] or 10000 < elem[2] or 10000 < elem[3]:
        #     print(-1)
        # elif elem[0] == elem[]
        print(turret(elem))