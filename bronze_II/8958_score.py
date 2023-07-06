# -*- coding: utf-8 -*-

def cal_score(s):
    total = 0
    score = 1
    for i in range(len(s)):
        if s[i] == "O":
            total += score
            score += 1
        else:
            score = 1

    return total

if __name__ == "__main__":
    n = int(input())

    scores = []
    for i in range(n):
        scores.append(cal_score(input()))

    for score in scores:
        print(score)