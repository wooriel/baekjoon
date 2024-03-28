# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    n = int(stdin.readline().rstrip())

    max_scores = []
    stairs = []
    max_score = 0
    for i in range(n):
        inp = int(stdin.readline().rstrip())
        if i == 0:
            max_score = inp
            max_scores.append(max_score)
            stairs.append(inp) 
        elif i == 1:
            max_score = max_scores[i-1] + inp
            max_scores.append(max_score)
            stairs.append(inp)
        elif i == 2:
            max_score = max(stairs[i-1] + inp, max_scores[i-2] + inp)
            stairs.append(inp)
            max_scores.append(max_score)
        else:
            max_score = max(max_scores[i-3] + stairs[i-1] + inp, max_scores[i-2] + inp)
            stairs.append(inp)
            max_scores.append(max_score)

    print(max_score)