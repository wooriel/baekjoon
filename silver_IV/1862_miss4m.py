# -*- coding: utf-8 -*-

def count4(num=str):
    count = 0
    # count_self = 0
    nextsub = 0
    for i in range(len(num)):
        if int(num[i]) > 4:
            count += pow(10, len(num[i:])-1)
        if i != 0:
            # size: 얼마만큼 스킵되는지
            # amount: 해당 자릿수의 수 (2000이면 2) * 9의 자릿수 승 (1000이니까 3)만큼 빠짐
            size = pow(10, len(num[i:])-1)
            amount = 0
            for j in range(len(num[:i])):
                amount += pow(9, len(num[:i]) - j - 1) * int(num[j])
            
            count += size * amount
            

    return count # + count_self

if __name__ == "__main__":
    miss4 = int(input())
    occur4 = count4(str(miss4))

    print(miss4 - occur4)