# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict

if __name__ == "__main__":
    lst = list(map(int, stdin.readline().split()))
    lst.sort()
    n = len(lst)
    max_diff = (lst[7] + lst[6] - lst[1] - lst[0])*0.5

    if len(set(lst)) == 1:
        print("1.0")
    else:
        all_team = set()
        team = defaultdict(set)
        for i in range(0, n-1):
            for j in range(i+1, n):
                comp = (i, j, (lst[i] + lst[j])*0.5)
                team[i].add(comp)
                team[j].add(comp)
                all_team.add(comp)

        res = []
        for i in range(n):
            a = team[i]
            b = list(all_team - a)
            a = list(a)
            min_diff = max_diff
            idx_set = [0, 1, 6, 7]
            for elem in a:
                for elem2 in b:
                    cur = abs(elem[2]-elem2[2])
                    if cur < min_diff:
                        if elem[1] != elem2[0] and elem[1] != elem2[1]:
                            min_diff = cur
                            # 두번째 index 겹치는 경우 있는거 같음 ㅠㅠ
                            idx_set = [elem[0], elem[1], elem2[0], elem2[1]]
                    if min_diff == 0.0:
                        break
                if min_diff == 0.0:
                    break
            # calculate score based on min_value of two team difference for idx i
            ans_i = 1 - min_diff*0.1
            res.append((ans_i, [lst[elem3] for elem3 in idx_set]))

        res.sort(key=lambda x: x[0], reverse=True)

        # find minimum value
        # you can terminate when all values in lst can be removed
        cur_sat = res[0][0]
        for elem in res[0][1]:
            lst.remove(elem)
        for i in range(1, n):
            cur_sat = res[i][0]
            vals = res[i][1]
            for elem in vals:
                try:
                    lst.remove(elem)
                except ValueError:
                    pass
            if len(lst) == 0:
                break

        _str = "{:.1f}".format(cur_sat)
        if _str == str(cur_sat):
            print(_str)
        else:
            print("{:.2f}".format(cur_sat))
