# -*- coding: utf-8 -*-
from collections import deque


def remove_flip(que):
    
    count = 0
    while len(que) != 1:
        if count % 2 == 0:
            que.popleft()
        else:
            que.rotate(-1)
            # elem = que.pop()
            # que.append(elem)
        count += 1

    return que.pop()

if __name__ == "__main__":
    n = int(input())
    d = deque([i for i in range(1, n+1)])

    
    elem = remove_flip(d)

    print(elem)