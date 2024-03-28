# -*- coding: utf-8 -*-
from sys import stdin

def switch01(lst):
    temp = lst[0]
    lst[0] = lst[1]
    lst[1] = temp

    return lst

def switch02(lst):
    temp = lst[0]
    lst[0] = lst[2]
    lst[2] = temp

    return lst

if __name__ == "__main__":
    dist = int(stdin.readline())

    cost_map = [] # 2D map
    total = 0
    res = []
    for i in range(dist):
        cost = list(map(int, stdin.readline().split()))
        cost_idx = [(cost[i], i) for i in range(len(cost))]
        cost_idx.sort(key=lambda x: x[0])
        cost_map.append(cost_idx)
        # append minimum cost and its index
        # res.append(costs[min_idx], min_idx)

    for j in range(1, dist):
        if j + 1 < dist and cost_map[j-1][0][1] == cost_map[j][0][1] == cost_map[j+1][0][1]:
            cost_map[j] = switch01(cost_map[j])
        elif cost_map[j-1][0][1] == cost_map[j][0][1]:
            dif1_1 = cost_map[j-1][1][0] - cost_map[j-1][0][0]
            dif1_2 = cost_map[j][1][0] - cost_map[j][0][0]
            noverlap1 = j-1 == 0 # not overlapping = True
            if noverlap1 == False:
                noverlap1 = cost_map[j-2][0][1] != cost_map[j-1][1][1]
            noverlap2 = cost_map[j+1][0][1] != cost_map[j][1][1]
            dif2_1, dif2_2 = -1, -1
            if noverlap1 == False:
                dif2_1 = cost_map[j-1][2][0] - cost_map[j][0][0]
            if noverlap2 == False:
                dif2_2 = cost_map[j][2][0] - cost_map[j][0][0]
            
            if dif1_1 < dif1_2 and noverlap1:
                cost_map[j-1] = switch01(cost_map[j-1])
            elif dif1_1 > dif1_2 and noverlap2:
                cost_map[j] = switch01(cost_map[j])
            elif noverlap1 == False and noverlap2 == False:
                if dif2_1 < dif2_2:
                    cost_map[j-1] = switch02(cost_map[j-1])
                else:
                    cost_map[j] = switch02(cost_map[j])
            elif noverlap1 == False:
                if dif2_1 < dif1_2:
                    cost_map[j-1] = switch02(cost_map[j-1])
                else:
                    cost_map[j] = switch01(cost_map[j])
            else: # noverlap2 == False
                if dif2_2 < dif1_1:
                    cost_map[j] = switch02(cost_map[j])
                else:
                    cost_map[j-1] = switch01(cost_map[j-1])

    total = 0
    for k in range(dist):
        total += cost_map[k][0][0]

    print(total)
                