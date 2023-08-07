# -*- coding: utf-8 -*-

def num_big(lst, n):
    big = ['0' for i in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            else:
                if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
                    big[i] = str(int(big[i]) + 1)
        big[i] = str(int(big[i]) + 1)


    return big

# def rank(lst, n):
#     ranks = [0 for i in range(n)]

#     rank = 1
#     count = 0
#     cur_max = 0
#     while rank <= n:
#         cur_max = max(lst)
#         idx = lst.index(cur_max)
#         ranks[idx] = str(rank)
#         lst[idx] = -1
#         count += 1
#         while True:
#             try:
#                 same_rank_idx = lst.index(cur_max)
#                 ranks[same_rank_idx] = str(rank)
#                 lst[same_rank_idx] = -1
#                 count += 1
#             except:
#                 rank += count
#                 count = 0
#                 break

#     return ranks


if __name__ == "__main__":
    n = int(input())
    lst = []

    for i in range(n):
        lst.append(tuple(map(int, input().split())))

    res = num_big(lst, n)

    # ranks = rank(res, n)
    
    strranks = " ".join(res)
    print(strranks)
