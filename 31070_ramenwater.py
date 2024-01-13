# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict
from collections import deque
from itertools import combinations
# from math import comb

def calc_tree_level(d:dict):
    ancs = defaultdict(list)

    to_visit = deque()
    to_visit.append(1)
    visited = set()
    visited.add(1)
    while len(to_visit) != 0:
        cur = to_visit.popleft()
        check = set(d[cur]) - visited
        for elem in check:
            ancs[elem].extend(ancs[cur])
            ancs[elem].append(cur)
            to_visit.append(elem)
            visited.add(elem)
    return ancs
        

if __name__ == "__main__":
    n, k = map(int, stdin.readline().split())

    con_room = defaultdict(list)
    while True:
        line = stdin.readline().rstrip()
        if line == "":
            break
        else:
            a, b = map(int, line.split())
            con_room[a].append(b)
            con_room[b].append(a)

    friends = list(con_room.keys())
    friends.remove(1)

    ancpath = calc_tree_level(con_room)
    # comb 순서 ancester 길이 긴 순으로
    combs = list(combinations(friends, k))

    # for elem in combs:
    #     for comp in elem:
