# -*- coding: utf-8 -*-
# from collections import defaultdict
# from statistics import median
from sys import stdin

if __name__ == "__main__":
    n = int(input())

    numdict = {}
    keylist = []
    sum = 0
    rmin, rmax = 0, 0

    # first elem here
    newinp = int(stdin.readline())
    rmin, rmax = newinp, newinp
    keylist.append(newinp)
    numdict[newinp] = 1
    sum = newinp

    for i in range(n-1):
        newinp = int(stdin.readline())
        # change min and max (range)
        if rmin > newinp:
            rmin = newinp
        if rmax < newinp:
            rmax = newinp

        # median
        keylist.append(newinp)

        # insert in numdict (mode)
        if newinp in numdict:
            numdict[newinp] += 1
        else:
            numdict[newinp] = 1

        # add to sum
        sum += newinp

    # mean, median, mode, range
    print(round(sum/n))

    # k = list(numdict.keys())
    keylist.sort()
    print(keylist[n//2])

    v = list(numdict.values())
    maxval = max(v)
    idxlst = []
    add = 0
    while True:
        try:
            idx = v.index(maxval)
            del v[idx]
            idxlst.append(idx + add)
            add += 1
        except ValueError:
            break
    modekey = []
    k2 = list(numdict.keys())
    for i in range(len(idxlst)):
        modekey.append(k2[idxlst[i]])
    if len(modekey) == 1:
        print(min(modekey))
    else:
        modekey.remove(min(modekey))
        print(min(modekey))

    print(rmax - rmin)