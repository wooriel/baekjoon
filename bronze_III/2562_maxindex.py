#-*- coding: utf-8 -*-

if __name__ == "__main__":
    LENGTH = 9

    max_num = 0
    max_idx = 0
    for i in range(LENGTH):
        inp_num = int(input())
        if max_num < inp_num:
            max_num = inp_num
            max_idx = i+1

    print(max_num)
    print(max_idx)