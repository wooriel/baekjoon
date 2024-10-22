# -*- coding: utf-8 -*-
from sys import stdin


# def return_mins(_set: set):
#     _lst = list(_set)
#     _lst.sort(key=lambda x: x[1])
#     _lst.sort(key=lambda x: x[0])
#     x_min = _lst[0]
#     _lst.sort(key=lambda x: x[1])
#     y_min = _lst[0]
#     d_set = set()
#     for elem in _lst:
#         if elem[0] >= x_min[0] and elem[1] >= x_min[1]:
#             d_set.add(elem)
#         _set = _set.difference(d_set)
#     if x_min != y_min:
#         for elem in _lst:
#             if elem[0] >= y_min[0] and elem[1] >= y_min[1]:
#                 d_set.add(elem)
#         _set = _set.difference(d_set)
#         _set.add(y_min)
#     _set.add(x_min)
#     return _set


if __name__ == "__main__":
    a = stdin.readline().rstrip()
    b = stdin.readline().rstrip()
    l_a = len(a)
    l_b = len(b)

    _map = []
    for i in range(l_a):
        lst = [0 for j in range(l_b)]
        _map.append(lst)

    _min = (0, 0)
    for i in range(l_a):
        for j in range(l_b):
            prev_r, prev_c, lst_ridx, lst_cidx = 0, 0, {
                (-1, -1)}, {(-1, -1)}
            if i != 0:
                prev_r, lst_ridx = _map[i-1][j]
            if j != 0:
                prev_c, lst_cidx = _map[i][j-1]
            inc_set = set()
            c_set = set()
            if prev_r > prev_c:
                cur = prev_r
                c_set = lst_ridx
            elif prev_c > prev_r:
                cur = prev_c
                c_set = lst_cidx
            else:
                cur = prev_r
                c_set.update(lst_ridx)
                c_set.update(lst_cidx)
            for elem in c_set:
                for c_r in range(elem[0]+1, i+1):
                    for c_c in range(elem[1]+1, j+1):
                        if a[c_r] == b[c_c]:
                            inc_set.add((c_r, c_c))
                            break
            if len(inc_set) == 0:
                _map[i][j] = [cur, c_set]
            else:
                # if len(inc_set) > 2:
                #     inc_set = return_mins(inc_set)
                _map[i][j] = [cur+1, inc_set]
            c_lst = list(_map[i][j][1])
            c_lst.sort(key=lambda x: x[0])
            _min = c_lst[0]
            if _min[1] == l_b-1:
                break
    print(_map[_min[0]][_min[1]][0])
    # print(_map[l_a-1][l_b-1][0])
