
def find_k_index(n, k, lst):
    max_nums = sorted(lst)[n-k:] # 가장큰 k개의 원소 (k개 만큼만 계산)
    lst2 = lst.copy()
    k_lst = [] # 가장 큰 k개의 원소들의 index
    for i in range(k):
        connected_num = max_nums[i]
        idx = lst2.index(connected_num) # 원래 인덱스
        lst2[idx] = -1 # 중복있을때 찾지 말라고
        k_lst.append(idx)

    return k_lst

if __name__ == "__main__":
    n, k = input().split(" ")
    n = int(n)
    k = int(k)

    lst = input().split(" ")
    lst = list(map(int, lst))

    k_lst = find_k_index(n, k, lst)
    for idx in k_lst:
        print(lst[idx])

    # k개 만큼의 subset을 greedy하게 구할것
    two_elems = set()
    max_nums = sorted(lst)[n-k:]
    for i in range(k):
        for j in range(n):
            two_elems.add((i, j))

    

     # 가장큰 k개의 원소
    # # 중요도가 같은게 있을때 연결
    # connected_idx = [0 for int in range(n)]
    # connected_lst = []
    # lst2 = lst.copy()
    # if k != 1:
    #     for j in range(0, k):
    #         # 같은 index있는지 확인
    #         connected_comp = []
    #         for k in range(2):
    #             connect_num = max_nums[j]
    #             try:
    #                 connect_idx = lst2.index(connect_num)
    #                 connected_comp.append(connect_idx)
    #                 lst2[connect_idx] = -1
    #             except ValueError:
    #                 break
            
    #         if len(connected_comp) == 1:
    #             # connected_comp = connected_comp.append(connected_comp[0]) # 추후 꼬이는 경우 있는지 확인 위해
    #             # connected_lst.extend(connected_comp)
    #             # 자기 자신이랑 연결되어있음
    #             itself = connected_comp[0]
    #             connected_idx[itself] = itself+1
    #         elif len(connected_comp) == 2 and (len(connected_lst) == 0 or connected_lst[-1] < connected_comp[0]):
    #             connected_lst.extend(connected_comp) # 추후 꼬이는 경우 있는지 확인 위해
    #             comp1 = connected_comp[0]
    #             comp2 = connected_comp[1]
    #             connected_idx[comp1] = comp2+1
    #             connected_idx[comp2] = comp1+1
    #         elif len(connected_comp) == 2 and len(connected_lst) != 0 and connected_lst[-1] > connected_comp[0]:
    #             comp1 = connected_comp[0]
    #             comp2 = connected_comp[1]
    #             connected_idx[comp1] = comp1+1
    #             connected_idx[comp2] = comp2+1

    # for i in range(n):
    #     print(connected_idx[i])
