# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    cases = int(stdin.readline())

    res = []
    for i in range(cases):
        n = int(stdin.readline())

        lim = pow(n, 2) // 2 # + n // 2
        # if n % 2 == 1:
        #     lim += 1
        
        lst = [] # [1]
        nums = [] # [1]
        num_coord = []
        # j = 1
        # while j < lim+1:
        for j in range(1, lim+1): # (2, lim+1)
            x1, y1 = (j-1) // n, (j-1) % n

            # if j % n >= n // 2:
            #     j += n // 2
            cur = 0
            x2, y2 = 0, 0
            for k in range(1, lim+1):
                if k <= len(lst):
                    cur = lst[k-1]
                else:
                    cur += k
                    lst.append(cur)
                if j <= cur:
                    x2 = k - 1
                    nth = j - (cur - k) # 1st, 2nd, ...
                    x2 -= (nth-1)
                    y2 = nth-1
                    break
            if x1 == x2 and y1 == y2:
                nums.append(j)
                num_coord.append([y1, x1])
            # j += 1
            #     j += n
            # else:
            #     j += 1

        if n % 2 == 1:
            nums.append(lim+1)
            # num_coord.pop() # 정중앙 좌표 버리기
        while len(num_coord) > 0:
            x1, y1 = num_coord.pop()
            print("{} {}".format(x1, y1))
            psym_num = ((n-1) - y1)*n + (n-1) - x1 + 1
            nums.append(psym_num)
        

        for i in range(len(nums)):
            print(nums[i], end='')
            if i != len(nums)-1:
                print(' ', end='')

        # 사분면으로 나누면 첫번째, 네번째, 거의 원의 궤적처럼, 약수와는 정확히 겹치지 않는 위치