#-*- coding: utf-8 -*-
def starline(num):
    star = ''
    for i in range(num):
        star += "*"

    return star

if __name__ == "__main__":
    numstar = int(input())

    for i in range(1, numstar+1):
        print(starline(i))