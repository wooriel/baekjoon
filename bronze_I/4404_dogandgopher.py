# -*- coding: utf-8 -*-
from sys import stdin
import math


if __name__ == "__main__":
    gx, gy, dx, dy = map(float, stdin.readline().split())
    # gx2, gy2, dx2, dy2 = gx*gx, gy*gy, dx*dx, dy*dy

    # mx, my = -10001, -10001
    sx, sy = -10001, -10001
    dist = math.inf
    while True:
        try:
            _dx, _dy = map(float, stdin.readline().split())
            # _dx2, _dy2 = _dx*_dx, _dy*_dy
            val1 = math.pow((gx-_dx), 2) + math.pow((gy-_dy), 2)
            val2 = math.pow((dx-_dx), 2) + math.pow((dy-_dy), 2)
            if val1*4 <= val2 and dist > val1:  # < does not matter
                sx, sy = _dx, _dy
                dist = val1
        except:
            break

    # mx2, my2 = mx*mx, my*my
    # val1 = abs(gx2 - mx2 + gy2 - my2)
    # val2 = abs(dx2 - mx2 + dy2 - my2)

    if sx != -10001:
        print(
            "The gopher can escape through the hole at ({0:.3f},{1:.3f}).".format(sx, sy))
    else:
        print("The gopher cannot escape.")
