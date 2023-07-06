# -*- coding: utf-8 -*-

def using_dict(word):
    alp = {}
    for i in range(len(word)):
        if word[i] not in alp:
            alp[word[i]] = 1
        else:
            alp[word[i]] = alp.get(word[i]) + 1

    # take the values
    max_val = max(alp.values())
    # max_alp = alp.index(max)

    max_alps = [alpha for alpha in alp.items() if alpha[1] == max_val]
    if len(max_alps) == 1:
        return max_alps[0][0]
    else:
        return '?'


if __name__ == "__main__":
    word = input().upper()

    res = using_dict(word)
    print(res)