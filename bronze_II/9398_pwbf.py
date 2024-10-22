# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict

if __name__ == "__main__":
    n = int(stdin.readline())

    for i in range(n):
        chr_type = defaultdict(set)
        pw = stdin.readline().rstrip()
        for j in range(len(pw)):
            cur = pw[j]
            if cur.isupper():
                chr_type['up'].add(j)
            elif cur.islower():
                chr_type['lo'].add(j)
            elif type(int(cur)) == int:
                chr_type['nu'].add(j)
            else:
                print('it cannot enter here :)')

        u_set = chr_type['up']
        l_set = chr_type['lo']
        n_set = chr_type['nu']

        # not meeting one of the requirements
        if len(u_set) == 0 or len(l_set) == 0 or len(n_set) == 0 or len(pw) < 6:
            print(0)
        else:
            min_len = len(pw)
            for a in u_set:
                for b in l_set:
                    for c in n_set:
                        _len = max(a, b, c) - min(a, b, c) + 1
                        if min_len > _len:
                            if _len <= 6:
                                min_len = 6
                                break
                            else:
                                min_len = _len
                    if min_len == 6:
                        break
                if min_len == 6:
                    break
            print(min_len)
