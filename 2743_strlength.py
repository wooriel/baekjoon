# -*- coding: utf-8 -*-

if __name__ == "__main__":
    word = input()

    count = 0
    while True:
        try:
            a = word[count]
            count += 1
        except IndexError:
            print(count)
            break