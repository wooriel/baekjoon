# -*- coding: utf-8 -*-
    

if __name__ == "__main__":
    n = int(input())

    words = set()
    for i in range(n):
        words.add(input())

    words = list(words)
    words.sort()

    words.sort(key=len)

    for w in words:
        print(w)
        