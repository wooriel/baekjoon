# -*- coding: utf-8 -*-
import string

if __name__ == "__main__":
    word = input()

    lst = []
    count = 0
    while True:
        try:
            character = word[count]
            if character in string.ascii_lowercase:
                lst.append(chr(ord(character) - 32))
            else:
                lst.append(chr(ord(character) + 32))
            count += 1
        except IndexError:
            break

    print("".join(lst))