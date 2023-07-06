#-*- coding: utf-8 -*-
def starline(num, max):
    blank = ''
    star = ''
    for i in range(max-num):
        blank += " "
    for i in range(num):
        star += "*"

    return blank+star

if __name__ == "__main__":
    starnum = int(input())

    for i in range(1, starnum+1):
        print(starline(i, starnum))