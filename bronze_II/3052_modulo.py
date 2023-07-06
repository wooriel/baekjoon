# -*- coding: utf-8 -*- 

if __name__ == "__main__":
    remainders = set()

    LENGTH = 10
    for i in range(LENGTH):
        remainders.add(int(input()) % 42)

    print(len(list(remainders)))