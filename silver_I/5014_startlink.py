# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque

if __name__ == "__main__":
    total, start, end, u, d = map(int, stdin.readline().split())

    nodes = deque()
    nodes.append((start, 0))
    visited = [-1 for i in range(total+1)] # idx 0은 안쓸예정

    ans = -1
    while len(nodes) > 0:
        cur, count = nodes.popleft()
        visited[cur] = count
        if cur == end:
            if ans == -1:
                ans = count
            else:
                if ans > count:
                    ans = count
        else:
            newnode1 = cur+u
            newnode2 = cur-d

            if newnode1 <= total and visited[newnode1] == -1:
                nodes.append((newnode1, count+1))
                visited[newnode1] = count+1
                # if newnode1 == end:
                #     if ans > count+1:
                #         ans = count+1
            if newnode2 > 0 and visited[newnode2] == -1:
                nodes.append((newnode2, count+1))
                visited[newnode2] = count+1
                # if newnode2 == end:
                #     if ans > count+1:
                #         ans = count+1

    if ans == -1:
        print('use the stairs')
    else:
        print(ans)