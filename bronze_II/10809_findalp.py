# -*- coding: utf-8 -*-

if __name__ == "__main__":
    word = input().upper()

    alp_pos = [-1 for elem in range(26)]
    for i in range(len(word)):
        if alp_pos[ord(word[i]) - ord('A')] == -1:
            alp_pos[ord(word[i]) - ord('A')] = i

    for i in range(len(alp_pos)):
        if i != len(alp_pos) - 1:
            print(alp_pos[i], end=" "),
        else:
            print(alp_pos[i])