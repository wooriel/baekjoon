# -*- coding: utf-8 -*-
from sys import stdin
import math
from collections import deque

if __name__ == "__main__":
    side = int(stdin.readline())

    tri = []
    for i in range(side):
        lst = []
        curstr = stdin.readline()
        for j in range(i+1):
            lst.append(curstr[j])
        tri.append(lst)

    ava_sp = math.factorial(side)
    numava = str(ava_sp)
    sum = 0
    for i in range(len(numava)):
        sum += int(numava[i])
    if sum % 3 != 0:
        print(0)
    else:
        dx = [1, 1, 0, 1]
        dy = [0, 1, 1, 1]
        wrong = False
        for j in range(side):
            for k in range(j+1):
                x, y = j, k
                if tri[x][y] == '1':
                    continue
                else:
                    check = 'R'
                    if tri[x][y] == 'R':
                        nx, ny = x+dx[0], y+dy[0]
                        nx2, ny2 = x+dx[1], y+dy[1]
                    else: # tri[s] == 'B'
                        check = 'B'
                        nx, ny = x+dx[2], y+dy[2]
                        nx2, ny2 = x+dx[3], y+dy[3]
                    if nx >= side or ny >= side or nx2 >= side or ny2 >= side: # out of range
                        wrong = True
                        break
                    else:
                        if tri[nx][ny] == '1' or tri[nx2][ny2] == '1':
                            wrong = True
                            break
                        else:
                            if tri[nx][ny] == check and tri[nx2][ny2] == check:
                                tri[nx][ny] = '1'
                                tri[nx2][ny2] = '1'
                            else:
                                wrong = True
                                break
        if wrong == True:
            print(0)
        else:
            for m in range(len(side)):
                try:
                    _ = int(tri[m])
                except ValueError:
                    print(0)
            print(1)
                
