# -*- coding:utf-8 -*-
from sys import stdin
from collections import defaultdict

if __name__ == "__main__":
    n = int(stdin.readline())

    res = []
    for m in range(n):
        w, h, tile = map(int, stdin.readline().split())
        
        node = defaultdict(list)
        new_idx = 0
        for k in range(tile):
            cur_i, cur_j = map(int, stdin.readline().split())
            put = False
            idx = -1
            for ne in range(len(node.keys())):
                for elem in node[ne]:
                    if abs(cur_i - elem[0]) + abs(cur_j - elem[1]) < 2:
                        lst = node[ne]
                        if put == False:
                            lst.append((cur_i, cur_j))
                        if idx != -1:
                            lst = lst.extend(node[idx])
                            node[idx] = []
                            idx = ne
                        # node[ne] = lst
                        put = True
                        if idx == -1:
                            idx = ne
                        break
            if not put:
                # idx = len(node.keys())
                node[new_idx] = [(cur_i, cur_j)]
                new_idx += 1
        count = 0
        for f in node.values():
            if f != []:
                count += 1
        res.append(count)

    for worm_num in res:
        print(worm_num)


# def exists(tup, trees):
#     for i in range(len(trees)):
#         if tup in trees[i]:
#             return 1
#     return 0


# def build_tree(cur, w, h, case, tset=set()):
#     """_summary_

#     Args:
#         cur (_type_): _description_
#         w (_type_): _description_
#         h (_type_): _description_
#         block (_type_): _description_
#         tset (_type_, optional): _description_. Defaults to set().

#     Returns:
#         tset: _description_
#     """
#     if cur not in case or cur[0] > w or cur[1] > h:
#         return 
#     else:
#         tset.add(cur)
#         build_tree((cur[0] + 1, cur[1]), w, h, case, tset)
#         build_tree((cur[0], cur[1] + 1), w, h, case, tset)
#     return tset

# if __name__ == "__main__":
#     test_cases = int(input())

#     num_cabbage = []
#     for i in range(test_cases):
#         # input rectangle_cabbage(rc) = width, height, num_cabbage
#         rc = list(map(int, input().split()))
#         case = []
#         # input cases
#         for j in range(rc[2]):
#             case.append(tuple(map(int, input().split())))

#         trees = []
#         for elem in case:
#             # check for existance
#             if exists(elem, trees) == 0:
#                 tree = build_tree(elem, rc[0], rc[1], case, set())
#                 trees.append(tree)

#         num_cabbage.append(len(trees))

#     for i in range(len(num_cabbage)):
#         print(num_cabbage[i])