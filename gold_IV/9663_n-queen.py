# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque
from copy import deepcopy


def dfs(i):
    global COUNT
    if i == n:
        COUNT += 1
        return

    for j in range(n):
        diagR = (n-1)-i+j
        diagL = i+j
        if not usedJ[j] and not usedR[diagR] and not usedL[diagL]:
            usedJ[j] = 1
            usedR[diagR] = 1
            usedL[diagL] = 1
            dfs(i+1)
            usedJ[j] = 0
            usedR[diagR] = 0
            usedL[diagL] = 0


if __name__ == "__main__":
    n = int(stdin.readline())

    usedJ = [0 for i in range(n)]
    usedR, usedL = [0 for i in range(2*n-1)], [0 for i in range(2*n-1)]

    COUNT = 0
    dfs(0)

    # # setting the board
    # _board = []
    # for i in range(n):
    #     lst = [0 for j in range(n)]
    #     _board.append(lst)

    # usedI = set() # used index in row
    # usedJ = set() # used index in column
    # # also check if (n-1 - i) + j and (n-1 - j) + i is same
    # usedR = set()
    # usedL = set()
    # if the value is same, queen is at the same diagonal
    # https://www.acmicpc.net/board/view/126498

    # # count the number of possibilities
    # _cnt = 0

    # # usedI, usedJ = [0 for i in range(n)], [0 for i in range(n)]
    # # usedR, usedL = [0 for i in range(2*n-1)], [0 for i in range(2*n-1)]

    # queen = deque()  # holds tuple of (list of queens:list, num queen:int)
    # for j in range(n):
    #     # usedI, usedJ = [0 for i in range(n)], [0 for i in range(n)]
    #     usedJ = ['0' for i in range(n)]
    #     usedR, usedL = ['0' for i in range(2*n-1)], ['0' for i in range(2*n-1)]
    #     # usedI[0] = 1
    #     usedJ[j] = '1'
    #     r = (n-1) + j
    #     l = j
    #     usedR[r] = '1'
    #     usedL[l] = '1'
    #     # queen.append([(0, j, r, l)])
    #     # queen.append([usedI, usedJ, usedR, usedL, 0])
    #     queen.append([usedJ, usedR, usedL, 0])

    # while len(queen) > 0:
    #     # _lst = queen.popleft()
    #     # usedI, usedJ, usedR, usedL, i = queen.popleft()
    #     usedJ, usedR, usedL, i = queen.popleft()

    #     # build visited function
    #     # usedI, usedJ, usedR, usedL = set(), set(), set(), set()

    #     # for i in range(len(_lst)):
    #     #     usedI.add(_lst[i][0])
    #     #     usedJ.add(_lst[i][1])
    #     #     usedR.add(_lst[i][2])
    #     #     usedL.add(_lst[i][3])

    #     # if adding queen is available, add into deque
    #     # i = _lst[-1][0]+1
    #     i += 1
    #     if i < n:
    #         for j in range(n):
    #             rdiag = (n-1) - i + j
    #             ldiag = i + j
    #             # if i not in usedI and j not in usedJ and rdiag not in usedR and ldiag not in usedL:
    #             # if usedI[i] == 0 and usedJ[j] == 0 and usedR[rdiag] == 0 and usedL[ldiag] == 0:
    #             if usedJ[j] == 0 and usedR[rdiag] == 0 and usedL[ldiag] == 0:
    #                 # set queen
    #                 # usedI.add(i)
    #                 # usedJ.add(j)
    #                 # usedR.add(rdiag)
    #                 # usedL.add(ldiag)
    #                 # if len(_lst) + 1 == n:
    #                 #     _cnt += 1
    #                 # if usedI[-1] == 1:
    #                 #     cnt += 1
    #                 if i == n-1:
    #                     _cnt += 1
    #                 else:
    #                     # n_lst = deepcopy(_lst)
    #                     # n_lst.append((i, j, rdiag, ldiag))
    #                     # queen.append(n_lst)
    #                     # nusedI, nusedJ, nusedR, nusedL = deepcopy(usedI), deepcopy(usedJ), deepcopy(usedR), deepcopy(usedL)
    #                     nusedJ, nusedR, nusedL = deepcopy(
    #                         usedJ), deepcopy(usedR), deepcopy(usedL)
    #                     # nusedI[i] = 1
    #                     nusedJ[j] = 1
    #                     nusedR[rdiag] = 1
    #                     nusedL[ldiag] = 1
    #                     # queen.append([nusedI, nusedJ, nusedR, nusedL, i])
    #                     queen.append([nusedJ, nusedR, nusedL, i])

    print(COUNT)
