# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    n = int(stdin.readline())

    lst = []
    lst.append(10)

    if n == 1:
        print(lst[0])
    else:
        num_r = [i for i in range(9, 0, -1)]
        while n > 2:
            psum = sum(num_r)
            lst.append(psum)
            n -= 1
            temp = 0
            for i in range(len(num_r)):
                temp_next = num_r[i]
                if i == 0:
                    num_r[i] = psum - temp
                else:
                    num_r[i] = num_r[i-1] - temp
                temp = temp_next
        psum = sum(num_r)
        lst.append(psum)
        print(sum(lst) % 10007)
