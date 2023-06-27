# -*- coding:utf-8 -*-

# import numpy as np

def num_change_row(ground, inp):
    change = 0
    for l1, l2 in zip(ground, inp):
        if l1 != l2:
            change += 1

    return change


def calc_diff(chessb, x_start, y_start, end=1):
    # assert chessb.shape == (8,8)
    change = 0
    even_idx = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
    odd_idx = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
    for l in range(x_start, x_start+8):
        if l % 2 == 0:
            change += num_change_row(even_idx, chessb[l][y_start:y_start+8])
        else:
            if end:
                change += num_change_row(odd_idx, chessb[l][y_start:])
            else:
                change += num_change_row(odd_idx, chessb[l][y_start:y_start+8])
    if 32 < change:
        return 64-change
    else:
        return change

if __name__ == "__main__":
    n, m = map(int, input().split())
    board = []
    for a in range(n):
        board.append([*input()])

    # board = np.array(board)
    min_change = 64
    for i in range(n-8+1):
        for j in range(m-8+1):
            change = calc_diff(board, i, j, j+8-m==0)
            if min_change > change:
                min_change = change
    print(min_change)

# if __name__ == "__main__":
#     n, m = map(int, input().split())
#     board = []
#     for a in range(n):
#         board.append([*input()])

#     # board = np.array(board)
#     min_change = 64
#     for i in range(n-8+1):
#         for j in range(m-8+1):
#             change = 64
#             if i+8 != n and j+8 != m:
#                 # print(board[i:i+8-n,j:j+8-m].shape)
#                 change = calc_diff(board[i:i+8-n][j:j+8-m])
#             else:
#                 if i+8-n == 0 and j+8-m == 0:
#                     change = calc_diff(board[i:][j:])
#                 elif i+8-n == 0:
#                     change = calc_diff(board[i:][j:j+8-m])
#                 else: #j+8-m == 0
#                     change = calc_diff(board[i:i+8-n][j:])
#             if min_change > change:
#                 min_change = change
#     print(min_change)