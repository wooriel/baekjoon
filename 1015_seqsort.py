# -*- coding:utf-8 -*-

if __name__ == "__main__":
    length = int(input())
    arr = map(int, input().split(" "))

    # len = 3
    # arr = ['2', '3', '1']
    # len = 4
    # arr = ['2', '1', '3', '1']
    # len = 8
    # arr = ['4', '1', '6', '1', '3', '6', '1', '4']
    # newarr = "".join(sorted(arr))
    # numstr = ""
    # dic = {}
    # for strnum in arr:
    #     idx = newarr.find(strnum, dic.get(strnum, -1)+1)
    #     numstr += "{} ".format(idx)
    #     dic[strnum] = idx

    # print(numstr[:-1])

    tup_arr = []
    for i, elem in enumerate(arr):
        tup_arr.append((elem, i))

    new_tup_arr = sorted(tup_arr)
    for i in range(length):
        movement = new_tup_arr.index(tup_arr[i])
        if i == length - 1:
            print(movement, end="")
        else:
            print(movement, end=" ")