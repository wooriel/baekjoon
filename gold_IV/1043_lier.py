# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict
from collections import deque

if __name__ == "__main__":
    num_ppl, num_party = map(int, stdin.readline().split())

    ppl_set = set(map(int, stdin.readline().split()[1:]))

    if len(ppl_set) == 0:
        for i in range(num_party):
            lst = list(map(int, stdin.readline().split()))
        print(num_party)
    else:
        truth_lie_lst = [1 for i in range(num_party)] # 1: lie
        ppl_party = defaultdict(set)
        neighbor = defaultdict(set)
        visited = set()

        # ppl_party
        # dictionary key: index of people
        # dictionary value: party index

        # neighbor
        # dictrionary key: index of people
        # dictionary value: 
        for i in range(num_party):
            party_set = set(map(int, stdin.readline().split()[1:]))
            for elem in party_set:
                ppl_party[elem].add(i)
                neighbor[elem] = neighbor[elem].union(party_set)

        truth_deque = deque()        
        for elem in ppl_set:
            truth_deque.append(elem)

        while len(truth_deque) > 0:
            cur = truth_deque.popleft()
            if cur in visited:
                continue
            else:
                visited.add(cur)
                rel_party = ppl_party[cur]
                for elem in rel_party: # elem = party
                    if truth_lie_lst[elem] == 1:
                        truth_lie_lst[elem] = 0
                
                to_add = neighbor[cur] - ppl_set
                ppl_set.union(to_add) # update ppl_set
                for elem in to_add:
                    if elem not in visited:
                        truth_deque.append(elem)
                            


        # prev_party = defaultdict(set)
        # for i in range(num_party):
        #     lst = list(map(int, stdin.readline().split()))
        #     add_set = set(lst[1:])
        #     # update prev_party
        #     prev_party[i] = add_set
        #     int_set = ppl_set.intersection(add_set)
        #     if len(int_set) > 0: 
        #         # add additional people
        #         ppl_set = ppl_set.union(add_set)
        #         truth_lie_lst.append(0)
        #         # check truth_lie_lst
        #         end = len(truth_lie_lst)
        #         idx = 0
        #         newflag = True

        #         while idx < end:
        #             if idx == end - 1:
        #                 newflag = False
        #             if truth_lie_lst[idx] == 1:
        #                 if len(ppl_set.intersection(prev_party[idx])) != 0:
        #                     truth_lie_lst[idx] = 0
        #                     while 
        #             idx += 1
        #                     # update ppl_set and check prev
        #     else:
        #         truth_lie_lst.append(1)
                
        print(sum(truth_lie_lst))
                