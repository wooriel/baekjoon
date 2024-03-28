# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    num = int(stdin.readline())

    for i in range(num):
        intlen = int(stdin.readline())
        if intlen == 1:
            print(0)
        else:
            pal = ['0' for i in range(intlen)]
            sum = 0
            for j in range(1, intlen//2+1):
                pal[j-1] = str(j%10)
                pal[-j] = str(j%10)
                if j % 2 == 0:
                    sum += 2*j
                else:
                    sum -= 2*j
            if intlen % 2 == 1:
                strsum = str(abs(sum))
                if len(strsum) > 1:
                    newsum = abs(sum) % 10
                    to_subtract = (abs(sum) // 10) * 10
                    # if sum > 0:
                    #     for k in range(2, intlen//2+1, 2):
                    #         if to_subtract > 18:
                    #             to_subtract -= int(pal[k-1]) * 2
                    #             pal[k-1] = '0'
                    #             pal[-k] = '0'
                    #         else:
                    #             while to_subtract > 0 and int(pal[k-1]) > 0:
                    #                 pal[k-1] = str(int(pal[k-1])- 1)
                    #                 pal[-k] = str(int(pal[-k])- 1)
                    #                 to_subtract -= 2
                    #         if to_subtract == 0:
                    #             break
                    # else:
                    for k in range(3, intlen//2+1, 2):
                        if to_subtract > 18:
                            to_subtract -= int(pal[k-1]) * 2
                            pal[k-1] = '0'
                            pal[-k] = '0'
                        else:
                            while to_subtract > 0 and int(pal[k-1]) > 0:
                                pal[k-1] = str(int(pal[k-1])- 1)
                                pal[-k] = str(int(pal[-k])- 1)
                                to_subtract -= 2
                        if to_subtract == 0:
                            break
                    pal[j] = str(newsum)
                    print(int(''.join(pal)))
                    # print(int(''.join(pal))%11)
                else:
                    pal[j] = strsum
                    print(int(''.join(pal)))
                    # print(int(''.join(pal))%11)
            else:
                print(int(''.join(pal)))
                # print(int(''.join(pal))%11)