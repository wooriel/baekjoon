# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    nppl = int(stdin.readline())

    names = []
    for i in range(nppl):
        name = stdin.readline().rstrip()
        names.append(name)

    idx = 0
    output = ""
    temp = ""
    lie_flag = False
    for i in range(nppl):
        print("? {}".format(names[i]))
        ans = int(stdin.readline())
        if ans == 1:
            if lie_flag:
                output = names[i]
                break
            else:
                print("? {}".format(names[i]))
                ans = int(stdin.readline())
                if ans == 1:
                    output = names[i]
                    break
                else: # 1 0
                    print("? {}".format(names[i]))
                    ans = int(stdin.readline())
                    if ans == 1:
                        output = names[i]
                        break
                    else:
                        lie_flag = True

    if output == "":
        # lie_flag = True
        for i in range(nppl-1):
            print("? {}".format(names[i]))
            ans = int(stdin.readline())
            if ans == 1:
                output = names[i]
                break
        if output == "":
            print("! {}".format(names[-1]), flush=True)

    print("! {}".format(output), flush=True)

    # nppl*2-1 th question
    # if output == "":
    #     print("? {}".format(names[nppl-1]))
    #     ans = int(stdin.readline())
    #     if ans == 0:
    #         print("! {}".format(temp), flush=True)
    #     else:
    #         print("! {}".format(names[nppl-1]), flush=True)
    # else:
    #     print("! {}".format(output), flush=True)
    

    # while output == "" and idx < nppl:
    #     print("? {}".format(names[idx]))
    #     ans = int(stdin.readline())
    #     if ans == 0:
    #         print("? {}".format(names[idx]))
    #         ans = int(stdin.readline())
    #         if ans == 1:
    #             output = names[idx]
    #     else: # ans == 1:
    #         # ask again unless last one
    #         if idx == nppl - 1:
    #             output = names[idx]
    #         else:
    #             print("? {}".format(names[idx]))
    #             ans = int(stdin.readline())
    #             if ans == 1:
    #                 output = names[idx]
    #     idx += 1

    # print("! {}".format(output), flush=True)