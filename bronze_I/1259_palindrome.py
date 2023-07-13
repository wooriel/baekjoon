# -*- coding: utf-8 -*-

def is_palindrome(num):
    s_num = str(num)
    for i in range(len(s_num)//2):
        if s_num[i] != s_num[-(i+1)]:
            return "no"
    return "yes"

if __name__ == "__main__":
    ans = []
    while True:
        num = int(input())
        if num == 0:
            break
        else:
            ans.append(is_palindrome(num))

    for i in range(len(ans)):
        print(ans[i])