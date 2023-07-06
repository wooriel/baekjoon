# -*- coding: utf-8 -*- 

def rep_str(num, s):
    ret_str = ''
    for i in range(len(s)):
        for j in range(num):
            ret_str += s[i]
    
    return ret_str

if __name__ == "__main__":
    res_lst = []
    while True:
        try:
            lst = input().strip().split(" ")
            if len(lst) == 2:
                repeat = int(lst[0])
                string = lst[1]
                res_lst.append(rep_str(repeat, string))
        except EOFError:
            break

    for elem in res_lst:
        print(elem)