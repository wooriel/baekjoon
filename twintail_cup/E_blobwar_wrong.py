# -*- coding: utf-8 -*-
from sys import stdin
import math

def pin_edge(c, d, e):
    while c != 1:
        if [(c//2)//2, c//2, d-1] in e:
            return True
        c //= 2
        d -= 1
    
    return False

if __name__ == "__main__":
    depth, nblock, u, t = map(int, stdin.readline().split())

    edge = []
    pow_2 = [pow(2, i) for i in range(1, depth)]
    for i in range(nblock):
        e = list(map(int, stdin.readline().split()))
        s_depth = math.ceil(pow(e[0], 1/2)) # number of t = start depth of edge
        # if s_depth in pow_2:
        #     s_depth += 1
        e.append(s_depth)
        edge.append(e)

    # t_total = 0
    # for i in range(1, depth):
    #     t_total += pow(2, 2*i-1)*t
    # twinblob_total = (pow(2, depth)-2) * u + t_total
    twinblob_total = u * (depth - 1) # + t * (depth - 1 - nblock) # t에 대한 계산 필요함 - 안갈라질때마다 t 하나씩 빼면 되서 계산함

    count = 1
    tdepth = 0
    for i in range(2, depth+1):
        add = 0
        for j in range(pow(2, i-1)//2):
            count += 1
            if [count//2, count, i-1] in edge and [count//2, count+1, i-1] in edge: # i is depth, edge[-][2] = start of the depth
                add += 0
            elif pin_edge(count, i-1, edge): # parent in edge
                add += 0
            else:
                add += 1
            count += 1
        if count != 3:
            tdepth += math.ceil(add / pow(2, i-2))
        if add == 0:
            twinblob_total -= u * (depth - (i-1))
            break
    twinblob_total += (pow(2, tdepth) - 1) * t


    ponyblob_total = (pow(2, depth) - 2) * 2 * u - (depth - 1) * u
    no_double_edge_e = [pow(2, i) - 1 for i in range(1, depth)]

    for elem in edge:
        # twin
        # twinblob_total -= u
        # twinblob_total -= elem[2] * t
        # pony
        # ponyblob_total -= (pow(2, depth - elem[2]) - 1) * 2 * u
        ponyblob_total -= (pow(2, depth - elem[2]) - 1) * 2 * u
        if elem[1] in no_double_edge_e:
            ponyblob_total += (depth - elem[2]) * u 

    # print(twinblob_total)
    # print(ponyblob_total)

    if twinblob_total < ponyblob_total:
        print(":blob_twintail_aww:")
    elif twinblob_total == ponyblob_total:
        print(":blob_twintail_thinking:")
    else:
        print(":blob_twintail_sad:")