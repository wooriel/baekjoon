# -*- coding: utf-8 -*-

# v = [[1, 4], [3, 4], [3, 10]]
def solution(v):
    x = []
    y = []
    occ_x = set()
    occ_y = set()
    for elem in v:
        x.append(elem)
        y.append(elem)
        occ_x.add(elem)
        occ_y.add(elem)

    answer = []
    while len(occ_x) != 0:
        _x = occ_x.pop()
        x.remove(_x)
        if _x not in x:
            answer.append(_x)
        _y = occ_y.pop()
        y.remove(_y)
        if _y not in y:
            answer.append(_y)

    return answer