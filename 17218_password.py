# -*- coding: utf-8 -*-
from sys import stdin

def longsubstr(s1, s2):
    graph = []

    # calculate first line
    cur = s1[i]
    s2_0 = []
    if cur in s2:
        idx = s2.index()
        s2_0 = [0 for i in range(idx)]
        s2_1 = [1 for i in range(idx, len(s2))]
        s2_0.extend(s2_1)
    else:
        s2_0 = [0 for i in range(len(s2))]

    for i in range(len(s1)):
        s2_match = []
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                sfill_len = len(s1) - j
                sfill = [1 for k in range(sfill_len)]
                s2_match.extend(sfill)
                break
                # add previous
        graph.append(s2_match)
                


if __name__ == "__main__":
    str1 = stdin.readline().rstrip()
    str2 = stdin.readline().rstrip()

