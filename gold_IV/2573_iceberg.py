# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque
import copy

if __name__ == "__main__":
    r, c = map(int, stdin.readline().split())

    _map = []
    num_iceberg = 0
    for i in range(r):
        lst = list(map(int, stdin.readline().split()))
        for elem in lst:
            if elem != 0:
                num_iceberg += 1
        _map.append(lst)

    year = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    if num_iceberg == 0:
        print(year)
    else:
        while num_iceberg > 0:
            temp = []
            first_node = [-1, -1]
            for i in range(1, r-1):
                for j in range(1, c-1):
                    val = _map[i][j]
                    if val != 0:
                        # check neighbors
                        tosub = 0
                        for k in range(4):
                            nx, ny = i + dx[k], j + dy[k]
                            if _map[nx][ny] == 0:
                                tosub += 1
                        new_val = max(val - tosub, 0)
                        # _nmap[i][j] = new_val
                        temp.append((i, j, new_val))
                        if new_val == 0:
                            num_iceberg -= 1
                        if first_node == [-1, -1] and new_val > 0:
                            first_node = [i, j]
            
            # all melt
            if first_node == [-1, -1]:
                year = 0
            else:
                # update map and year
                for elem in temp:
                    _map[elem[0]][elem[1]] = elem[2]
                year += 1

                # check connectivity
                copy_iceberg = num_iceberg
                conn = deque()
                conn.append(first_node)
                visited = set()
                visited.add((first_node[0], first_node[1]))
                while len(conn) > 0:
                    x, y = conn.popleft()
                    copy_iceberg -= 1
                    for i in range(4):
                        nx, ny = x + dx[i], y + dy[i]
                        if (nx, ny) not in visited:
                            if _map[nx][ny] > 0:
                                conn.append([nx, ny])
                                visited.add((nx, ny))

                if copy_iceberg > 0:
                    break

        print(year)