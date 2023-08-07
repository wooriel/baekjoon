# -*- coding: utf-8 -*-

def find_rank(num, idx, lst):
    if num == 1:
        return 1
    else:
        init_order = [rank for rank in enumerate(lst)] # 앞이 index, 뒤가 rank
        new_index = init_order[idx]
        rank_order = init_order.copy()
        rank_order.sort(key=lambda x: x[1], reverse=True)

        print_order = []
        ro_idx = 0 # rank_order_index
        while ro_idx != num:
            curimp = init_order[0]
            maxtup = rank_order[ro_idx]
            if curimp[1] == maxtup[1]:
                print_order.append(curimp)
                init_order.remove(curimp)
                ro_idx += 1
            else:
                elem = init_order[0]
                init_order.remove(elem)
                init_order.append(elem)

        return print_order.index(new_index) + 1

if __name__ == "__main__":
    n = int(input())

    ans = []

    for i in range(n):
        num_doc, idx = map(int, input().split())
        lst = map(int, input().split())
        res = find_rank(num_doc, idx, lst)
        ans.append(res)

    for answer in ans:
        print(answer)