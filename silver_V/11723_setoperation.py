# -*- coding: utf-8 -*-
from sys import stdin
# from collections import defaultdict

# def bitop(bit, op, res):
#     if op == "all":
#         bit = (1 << 20) - 1
#     elif op == "empty":
#         bit = 0
#     else:
#         one_op, num = op.split()
#         num = int(num)
#         if one_op == "add":
#             bit |= 1 << num-1
#         elif one_op == "remove":
#             if bit & 1 << num-1:
#                 bit ^= 1 << num-1
#         elif one_op == "check":
#             if bit & 1 << num-1:
#                 res += "1"
#             else:
#                 res += "0"
#         elif one_op == "toggle":
#             bit ^= 1 << num-1
#             # if bit & 1 << num-1:
#             #     bit ^= 1 << num-1
#             # else:
#             #     bit |= 1 << num-1
#         else:
#             print("error")

#     return bit, res

if __name__ == "__main__":
    num_op = int(stdin.readline().rstrip())

    # res = ""
    bit = 0
    for i in range(num_op):
        op = stdin.readline().rstrip()
        if op == "all":
            bit = (1 << 20) - 1
        elif op == "empty":
            bit = 0
        else:
            one_op, num = op.split()
            num = int(num)
            if one_op == "add":
                bit |= 1 << num-1
            elif one_op == "remove":
                if bit & 1 << num-1:
                    bit ^= 1 << num-1
            elif one_op == "check":
                if bit & 1 << num-1:
                    print(1)
                else:
                    print(0)
            elif one_op == "toggle":
                bit ^= 1 << num-1
                # if bit & 1 << num-1:
                #     bit ^= 1 << num-1
                # else:
                #     bit |= 1 << num-1
            else:
                print("error")
        
        # bit, res = bitop(bit, op, res)
            
    # for i in range(len(res)):
    #     print(res[i])