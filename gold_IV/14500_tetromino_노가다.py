# -*- coding: utf-8 -*-
from sys import stdin

# def cal_val(nm, tetro_lst, s):
#     total = 0
#     for i in range(4):
#         x, y = s[0] + tetro_lst[i][0], s[1] + tetro_lst[i][1]
#         total += nm[x][y]

#     return total

if __name__ == "__main__":
    # tetro1 = [(0, 0), (0, 1), (0, 2), (0, 3)] # vertline
    # tetro2 = [(0, 0), (0, 1), (1, 0), (1, 1)] # square
    # tetro3 = [(0, 0), (1, 0), (2, 0), (2, 1)] # ㄴ
    # tetro4 = [(0, 0), (1, 0), (1, 1), (2, 1)] # ㄴㄱ
    # tetro5 = [(0, 0), (0, 1), (1, 1), (0, 2)] # ㅜ

    row, col = map(int, stdin.readline().split())
    num_map = []
    for k in range(row):
        lst = list(map(int, stdin.readline().split()))
        num_map.append(lst)

    max_val = 0
    for i in range(row):
        for j in range(col):
            if i + 2 < row and j + 1 < col:
                min_v, min2_v = 1001, 1001
                min_x, min_y = -1, -1
                min2_x, min2_y = -1, -1
                total = 0
                for m in range(i, i+3):
                    for n in range(j, j+2):
                        c_val = num_map[m][n]
                        total += c_val

                lst = [num_map[i][j] + num_map[i+2][j],
                       num_map[i][j+1] + num_map[i+2][j+1],
                       num_map[i][j] + num_map[i+1][j],
                       num_map[i+1][j] + num_map[i+2][j],
                       num_map[i][j+1] + num_map[i+1][j+1],
                       num_map[i+1][j+1] + num_map[i+2][j+1],
                       num_map[i][j] + num_map[i][j+1],
                       num_map[i+2][j] + num_map[i+2][j+1],
                       num_map[i][j] + num_map[i+2][j+1],
                       num_map[i][j+1] + num_map[i+2][j]]
                
                total -= min(lst)
                #         if min_v > c_val:
                #             if min2_v >= min_v:
                #                 min2_v = min_v
                #                 min2_x, min2_y = min_x, min_y
                #             min_v = c_val
                #             min_x, min_y = m, n
                #         else:
                #             if min2_v > c_val:
                #                 min2_v = c_val
                #                 min2_x, min2_y = m, n
                # if min2_x == i+1 and min_x == i+1:
                #     min2_v = min([num_map[i+0][j+0], num_map[i+0][j+1], num_map[i+2][j+0], num_map[i+2][j+1]])

                # total -= min_v
                # total -= min2_v

                if max_val < total:
                    max_val = total

            if i + 1 < row and j + 2 < col:
                min_v, min2_v = 1001, 1001
                min_x, min_y = -1, -1
                min2_x, min2_y = -1, -1
                total = 0
                for m in range(i, i+2):
                    for n in range(j, j+3):
                        c_val = num_map[m][n]
                        total += c_val

                lst = [num_map[i][j] + num_map[i][j+2],
                       num_map[i+1][j] + num_map[i+1][j+2],
                       num_map[i][j] + num_map[i][j+1],
                       num_map[i][j+1] + num_map[i][j+2],
                       num_map[i+1][j] + num_map[i+1][j+1],
                       num_map[i+1][j+1] + num_map[i+1][j+2],
                       num_map[i][j] + num_map[i+1][j],
                       num_map[i][j+2] + num_map[i+1][j+2],
                       num_map[i][j] + num_map[i+1][j+2],
                       num_map[i+1][j] + num_map[i][j+2]]
                
                total -= min(lst)
                        # if min_v > c_val:
                        #     if min2_v >= min_v:
                        #         min2_v = min_v
                        #         min2_x, min2_y = min_x, min_y
                        #     min_v = c_val
                        #     min_x, min_y = m, n
                        # else:
                        #     if min2_v > c_val:
                        #         min2_v = c_val
                        #         min2_x, min2_y = m, n
                # if min2_y == j+1 and min_y == j+1:
                #     min2_v = min([num_map[i+0][j+0], num_map[i+0][j+2], num_map[i+1][j+0], num_map[i+1][j+2]])
                
                # total -= min_v
                # total -= min2_v

                if max_val < total:
                    max_val = total

            if i + 3 < row:
                s = 0
                for m in range(i, i+4):
                    s += num_map[m][j]

                if max_val < s:
                    max_val = s

            if j + 3 < col:
                s = 0
                for m in range(j, j+4):
                    s += num_map[i][m]

                if max_val < s:
                    max_val = s

            # square
            if i + 1 < row and j + 1 < col:
                s = num_map[i][j] + num_map[i+1][j] + num_map[i][j+1] + num_map[i+1][j+1]

                if max_val < s:
                    max_val = s

    print(max_val)