# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict
from collections import deque


def calc_bacon(g, s, e):
    cur = (s, 0)
    visited = set()
    check_queue = deque()
    while cur[0] != e:
        cur_node = cur[0]
        visited.add(cur_node)
        for elem in g[cur_node]:
            if cur_node == e:
                return cur[1]
            else:
                if elem not in visited:
                    check_queue.append((elem, cur[1] + 1))
        cur = check_queue.popleft()
        while cur[0] in visited:
            cur = check_queue.popleft()

    return cur[1]

def min_bacon(g):
    minim = (-1, -1)
    for elem_s in g.keys():
        sum = 0
        for elem_e in g.keys():
            sum += calc_bacon(g, elem_s, elem_e)
        if minim[1] > sum or minim[1] == -1:
            minim = (elem_s, sum)
        elif minim[1] == sum:
            if minim[0] > elem_s:
                minim = (elem_s, sum)

    return minim[0]
    

if __name__ == "__main__":
    num_user, num_edge = map(int, stdin.readline().split())

    friends_dict = defaultdict(list)

    for i in range(num_edge):
        n1, n2 = map(int, stdin.readline().split())
        friends_dict[n1].append(n2)
        friends_dict[n2].append(n1)

    # calc_bacon(friends_dict, 1, 2)
    print(min_bacon(friends_dict))