# -*-coding: utf-8 -*-

if __name__ == "__main__":
    # a, b, c = map(int, input().split())
    a = int(input())
    b = int(input())
    c = int(input())

    strmul = str(a*b*c)
    lst = [0 for i in range(10)]
    for i in range(len(strmul)):
        lst[int(strmul[i])] += 1

    for j in range(len(lst)):
        print(lst[j])