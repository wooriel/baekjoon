# -*- coding: utf-8 -*-
from collections import deque

def is_balanced(inp):
    d = deque()
    for i in range(len(inp)):
        if inp[i] == '[' or inp[i] == '(':
            d.append(inp[i])
        elif inp[i] == ']' or inp[i] == ')':
            try:
                prev = d.pop()
                if prev == '[' and inp[i] == ')':
                    return False
                elif prev == '(' and inp[i] == ']':
                    return False
                else:
                    continue
            except:
                return False
        else: # string
            continue

    if len(list(d)) != 0:
        return False
    else:
        return True

if __name__ == "__main__":

    res = []

    while True:
        sentence = input()
        if sentence == '.':
            break
        res.append('yes') if is_balanced(sentence) else res.append('no')

    for r in res:
        print(r)
