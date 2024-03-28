# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict

def comp_str(str1, str2):
    dist = 4
    for i in range(4):
        if str1[i] == str2[i]:
            dist -= 1

    return dist


if __name__ == "__main__":
    cases = int(stdin.readline())
    for i in range(cases):
        num_ppl = int(stdin.readline())
        lst = list(stdin.readline().rstrip().split())

        # num_ppl > 16x3, all mbti have at least three people
        if num_ppl > 16 * 2:
            print(0)
        else:
            mbti_num = defaultdict(int)
            for i in range(len(lst)):
                mbti_num[lst[i]] += 1
            
            # if num_ppl > 16:
            #     ans = []
            #     min_dst = 4
            #     # minimum distance is 4 (two same, one totally different), three different(two has dist=1 with another one, that two is dist=2)
            #     keys = list(mbti_num.keys())
            #     for elem in keys:
            #         snum = mbti_num[elem]
            #         if snum > 1:
            #             if snum >= 3:
            #                 min_dst = 0
            #                 break
            #             else: # 2개 이상인게 2개 이상일수 있으니 break은 안함
            #                 ans.append(elem)
                        
            #     if min_dst != 4:
            #         for elem in keys:
            #             if elem not in ans:
            #                 for elem2 in ans:
            #                     dst = comp_str(elem, elem2)
            #                     if dst < min_dst:
            #                         min_dst = dst
            #     print(min_dst * 2)
            # else:
            min_dst = 16
            for i in range(len(lst)):
                for j in range(i+1, len(lst)):
                    cur_dst = 0
                    for k in range(j+1, len(lst)):
                        one, two, three = lst[i], lst[j], lst[k]
                        cur_dst += comp_str(one, two)
                        cur_dst += comp_str(two, three)
                        cur_dst += comp_str(one, three)
                        if min_dst > cur_dst:
                            min_dst = cur_dst
                        cur_dst = 0

            print(min_dst)