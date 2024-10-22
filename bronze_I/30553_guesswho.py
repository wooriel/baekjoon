# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    n, m, q = map(int, stdin.readline().split())

    ppl = []
    for i in range(n):
        p = stdin.readline().rstrip()
        ppl.append((i, p))

    for i in range(q):
        idx, ans = stdin.readline().rstrip().split()
        idx = int(idx)-1
        to_del = []
        for j in range(len(ppl)):
            node = ppl[j][1]
            if node[idx] != ans:
                to_del.append(j)
        while len(to_del) > 0:
            elem = to_del.pop()
            del ppl[elem]

    if len(ppl) == 1:
        print('unique')
        print(ppl[0][0]+1)
    else:
        print('ambiguous')
        print(len(ppl))
