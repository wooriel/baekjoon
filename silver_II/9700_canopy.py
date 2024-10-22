# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque

if __name__ == "__main__":
    case = 0
    while True:
        try:
            n = int(stdin.readline())
            case += 1
            _map = []
            _ones = set()
            for i in range(n):
                _str = stdin.readline().rstrip()
                _lst = []
                for j in range(n):
                    _cur = int(_str[j])
                    _lst.append(_cur)
                    if _cur == 1:
                        _ones.add((i, j))
                _map.append(_lst)

            dx = [-1, -1, -1, 0, 0, 1, 1, 1]
            dy = [-1, 0, 1, -1, 1, -1, 0, 1]
            count = 0
            while len(_ones) > 0:
                _cur = deque()
                visited = set()
                felem = _ones.pop()
                _cur.append(felem)
                while len(_cur) > 0:
                    _elem = _cur.popleft()

                    for i in range(8):
                        nx, ny = _elem[0]+dx[i], _elem[1]+dy[i]
                        if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                            if _map[nx][ny] == 1:
                                _cur.append((nx, ny))
                                visited.add((nx, ny))
                            else:
                                visited.add((nx, ny))
                if len(visited) > 0:
                    count += 1
                    _ones -= visited

            print("Case #{}: {}".format(case, count))
        except:
            break
