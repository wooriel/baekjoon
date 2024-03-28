# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque

if __name__ == "__main__":
    dest = stdin.readline().rstrip() # num in string format
    nbroken = int(stdin.readline())
    nnums = set([i for i in range(10)])
    bnums = set()
    if nbroken > 0:
        bnums = set(map(int, stdin.readline().split()))
    nnums -= bnums

    snum = 100
    min_move = 500000
    if int(dest) == snum:
        print(0)
    else:
        # move from snum
        smv = abs(int(dest) - snum)
        if smv < min_move:
            min_move = smv
        if nnums == set():
            print(min_move)
        else:
            # enter dest directly - high
            hnum = []
            no_num = False
            # neg = False
            for i in range(len(dest)):
                cur_dig = dest[i]
                if not no_num and int(cur_dig) in nnums:
                    hnum.append(cur_dig)
                else:
                    if no_num == False:
                        no_num = True
                        dif_max = abs(int(cur_dig) - max(nnums))
                        dif_min = abs(int(cur_dig) - min(nnums))
                        if dif_max > dif_min:
                            hnum.append(str(min(nnums)))
                            # if int(cur_dig) - min(nnums) < 0:
                                # neg = True
                        else:
                            hnum.append(str(max(nnums)))
                            # if int(cur_dig) - min(nnums) < 0:
                            #     neg = True
                    else:
                        hnum.append(str(min(nnums)))
                        # if neg == False:
                        #     hnum.append(str(min(nnums)))
                        # else:
                        #     hnum.append(str(max(nnums)))
            high_num = "".join(hnum)
            hmv = abs(int(high_num) - int(dest)) + len(str(int(high_num))) # 00 인경우 0으로 세어야함
            if hmv < min_move:
                min_move = hmv

            # enter dest directly - low
            lnum = []
            no_num = False
            for i in range(len(dest)):
                cur_dig = dest[i]
                if not no_num and int(cur_dig) in nnums:
                    lnum.append(cur_dig)
                else:
                    if no_num == False:
                        no_num = True
                        # replace prev_digit to small but nearest digit to prev_digit
                        ld_small = int(dest[i])
                        if i != 0:
                            ld_small = int(lnum.pop())
                        res_small = -1
                        for elem in nnums:
                            if ld_small - elem < 0:
                                break
                            else:
                                res_small = elem
                        if res_small == -1:
                            dif_max = abs(int(dest[i]) - max(nnums))
                            dif_min = abs(int(dest[i]) - min(nnums))
                            if dif_max > dif_min:
                                res_small = min(nnums)
                            else:
                                res_small = max(nnums)
                            # res_small = min(nnums) # 사실 이러면 이미 나가리임
                        if dest[i] == '1' and i == 0:
                            pass
                        else:
                            lnum.append(str(res_small))
                        # add cur_digit
                        if i != 0:
                            lnum.append(str(max(nnums)))
                        # dif_max = abs(int(cur_dig) - max(nnums))
                        # dif_min = abs(int(cur_dig) - min(nnums))
                        # if dif_max > dif_min:
                        #     lnum.append(str(min(nnums)))
                        # else:
                        #     lnum.append(str(max(nnums)))
                    else:
                        lnum.append(str(max(nnums)))
            low_num = "".join(lnum)
            if low_num != '':
                lmv = abs(int(dest) - int(low_num)) + len(str(int(low_num)))
                if lmv < min_move:
                    min_move = lmv

            # handle separately
            min_nnum = str(min(nnums))
            lnnums = list(nnums)
            lnnums.remove(int(min_nnum))
            min2_nnum = min(lnnums)
            len_lst = [min_nnum for i in range(len(dest))]
            suff = "".join(len_lst)
            scase = "".join([str(min2_nnum), suff])
            smv = int(scase) - int(dest) + len(scase)
            if smv < min_move:
                min_move = smv

            print(min_move)