# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    cases = int(stdin.readline())

    for i in range(cases):
        rdstr = stdin.readline().rstrip()
        lenarr = int(stdin.readline())
        lststr = stdin.readline().rstrip()
        # lst = lststr[1:-1].split(",")

        # if lststr == "[]":
        #     # check D
        #     flag = False
        #     for j in range(len(rdstr)):
        #         if rdstr[j] == 'D':
        #             flag = True
        #             break
        #     if flag:
        #         print('error')
        #     else:
        #         print(lststr)
        # elif len(lststr) == 3:
        #     count = 0
        #     for j in range(len(rdstr)):
        #         if rdstr[j] == 'D':
        #             count += 1
        #             if count > 1:
        #                 break
        #     if count > 1:
        #         print('error')
        #     elif count == 1:
        #         print('[]')
        #     else:
        #         print(lststr)
        # else:
        lst = lststr[1:-1].split(",")
        if '' in lst:
            lst = []
        lstart = 0
        rstart = len(lst)
        flag = 'L'
        for j in range(len(rdstr)):
            if rdstr[j] == 'D':
                if flag == 'L':
                    lstart += 1
                else:
                    rstart -= 1
            else: # 'R'
                if flag == 'L':
                    flag = 'R'
                else:
                    flag = 'L'

        if lstart < rstart:
            lst = lst[lstart:rstart]
            print('[', end = '')
            if flag == 'R':
                for i in range(len(lst)-1, -1, -1):
                    print(lst[i], end='')
                    if i != 0:
                        print(",", end='')
                    else:
                        print("]")
            else:
                for i in range(0, len(lst)):
                    print(lst[i], end='')
                    if i != len(lst) - 1:
                        print(',', end='')
                    else:
                        print("]")
        elif lstart == rstart: # 원소가 0개이고 delete안된경우
            print('[]')
            # lst = lststr[lstart:].split(",")
            # print("[{}]".format(lst[lstart]))
        # elif lstart == rstart + 1 and lstart <= len(lststr) and rstart >= 0:
        #     print("[]")
        else:
            print('error')