# -*- coding:utf-8 -*-

def calculate_d(ax, ay, bx, by, ox, oy):
    """_summary_

    Args:
        ax (double): _description_
        ay (double): _description_
        bx (double): _description_
        by (double): _description_
        ox (double): d 반대쪽에 있는 포인트 x coord
        oy (double): d 반대쪽에 있는 포인트 y coord
    """
    # calculate the middle point mx and my
    mx = (ax + bx) / 2.
    my = (ay + by) / 2.

    # calculate dx and dy using the middle point
    dx = 2. * mx - ox
    dy = 2. * my - oy

    return dx, dy
    # # check if dx and dy is in range
    # if abs(dx) < 5000 and abs(dy) < 5000:
    #     return dx, dy
    # else:
    #     return -1

def calculate_perimeter(ax, ay, bx, by, ox, oy):
    oa = pow(pow((ox - ax), 2) + pow((oy - ay), 2), 0.5)
    ob = pow(pow((ox - bx), 2) + pow((oy - by), 2), 0.5)
    return oa * 2. + ob * 2.


if __name__ == "__main__":
    # ax = 1
    # ay = 0
    # bx = 0
    # by = 2
    # cx = 2
    # cy = 2
    [ax, ay, bx, by, cx, cy] = list(map (float, input().split()))

    # check if all x or all y coords are same
    if ax == bx and ax == cx or ay == by and ay == cy:
        print(-1)
    elif (bx-ax != 0 and cx-ax != 0) and (by-ay)/(bx-ax) == (cy-ay)/(cx-ax):
        print(-1)
    else:
        # a가 가장 먼 포인트 일때
        tup_a = calculate_d(bx, by, cx, cy, ax, ay)
        perm_a = calculate_perimeter(bx, by, cx, cy, ax, ay)
    
        # b가 가장 먼 포인트 일때
        tup_b = calculate_d(cx, cy, ax, ay, bx, by)
        perm_b = calculate_perimeter(cx, cy, ax, ay, bx, by)

        # c가 가장 먼 포인트 일때
        tup_c = calculate_d(ax, ay, bx, by, cx, cy)
        perm_c = calculate_perimeter(ax, ay, bx, by, cx, cy)

        print(max(perm_a, perm_b, perm_c) - min(perm_a, perm_b, perm_c))