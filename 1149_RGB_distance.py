# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict


if __name__ == "__main__":
    dist = int(stdin.readline())

    cost_map = [] # 2D map
    for i in range(dist):
        cost = list(map(int, stdin.readline().split()))
        cost_map.append(cost)

    cost_idx = [[cost[i], i] for i in range(len(cost))]
    total = cost_idx


    cache = defaultdict(list)
    def help_cost(cost, idx, cidx):
        r = cost_map[idx][0]
        g = cost_map[idx][1]
        b = cost_map[idx][2]
        if idx == 0:
            if cidx == 0:
                if g < b:
                    return [cost+g, 1]
                else:
                    return [cost+b, 2]
            elif cidx == 1:
                if r < b:
                    return [cost+r, 0]
                else:
                    return [cost+b, 2]
            else:
                if r < g:
                    return [cost+r, 0]
                else:
                    return [cost+g, 1]
        if cache[idx] != []:
            return cache[idx]
        else:
            if cidx == 0:
                if g < b:
                    cache[idx] = [cost+g, 1]
                    return help_cost(cost+g, idx-1, 1)
                else:
                    cache[idx] = [cost+b, 2]
                    return help_cost(cost+b, idx-1, 2)
            elif cidx == 1:
                if r < b:
                    cache[idx] = [cost+r, 0]
                    return help_cost(cost+r, idx-1, 0)
                else:
                    cache[idx] = [cost+b, 2]
                    return help_cost(cost+b, idx-1, 2)
            else:
                if r < g:
                    cache[idx] = [cost+r, 0]
                    return help_cost(cost+r, idx-1, 0)
                else:
                    cache[idx] = [cost+g, 1]
                    return help_cost(cost+g, idx-1, 1)
    
    def get_cost():
        lvl = dist-1
        r = cost_map[lvl][0]
        g = cost_map[lvl][1]
        b = cost_map[lvl][2]

        return min(help_cost(r, lvl-1, 0)[0], help_cost(g, lvl-1, 1)[0], help_cost(b, lvl-1, 2)[0])


    print(get_cost())