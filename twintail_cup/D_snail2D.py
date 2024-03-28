# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    n, m = map(int, stdin.readline().split())
    pos = stdin.readline().rstrip()
    snail = [[0 for i in range(m)] for j in range(n)]

    snum = 1
    dir1, dir2 = 'L', 'R'
    r, c = n//2+1, m//2+1 # def: center, start of the loop
    if pos == 'U':
        r = 0
        while r < n:
            snail[r][c] = str(snum)
            snum += 1
            r += 1
    elif pos == 'D':
        r = n-1
        while r > -1:
            snail[r][c] = str(snum)
            snum += 1
            r -= 1
    elif pos == 'L':
        c = 0
        while c < m:
            snail[r][c] = str(snum)
            snum += 1
            c += 1
    else: # pos == 'R'
        c = m-1
        while c > -1:
            snail[r][c] = str(snum)
            snum += 1
            c -= 1

    # set starting num, dir
            
    while True:
        # check if the value is not zero
        if snail[r][c] != 0:
            break


    for i in range(n):
        print(" ".join(n[i]))