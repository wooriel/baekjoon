# -*- coding: utf-8 -*-
from sys import stdin

def calc_trial(n, m, c):
    # 7 2 2
    count = 0
    cur = (n, m, 0, 0)
    while cur[2] != n:
        # going
        going = (max(cur[0] - cur[1]*c, 0), 0, min(cur[2] + cur[1]*c, n), cur[1])
        if going[0] == 0:
            count += 1
            return count
        # returning
        comeback = (going[0] + 1, going[3], going[2] - 1, 0)
        if comeback[0] == cur[0]:
            return -1
        else:
            count += 2
            cur = comeback

    return count
    


if __name__ == "__main__":
    testcases = int(input())

    res = []
    for i in range(testcases):
        num_people, num_umbrella, capacity = map(int, stdin.readline().split())
        res.append(calc_trial(num_people, num_umbrella, capacity))

    for elem in res:
        print(elem)
