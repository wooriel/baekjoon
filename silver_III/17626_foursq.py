# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n = int(input())

    sq = [i**2 for i in range(1, int(pow(n, 1/2))+1)]

    res = []
    for i in range(len(sq)):
        if n == sq[i]:
            res.append(1)
            break
        for j in range(len(sq)):
            if n - sq[i] - sq[j] == 0:
                res.append(2)
                break
            for k in range(len(sq)):
                if n - sq[i] - sq[j] - sq[k] == 0:
                    res.append(3)
                    break

    if len(res) == 0:
        print(4)
    else:
        print(min(res))

    # i = 1
    # sq = [1]
    # power = 1
    # count = 0
    # cn = n
    # while cn != 0:
    #     while cn >= power:
    #         i += 1
    #         if count == 0:
    #             power = pow(i, 2)
    #             sq.append(power)
    #         else:
    #             power = sq[i-1]
    #     if count == 0:
    #         cn -= pow(i-1, 2)
    #     else:
    #         cn -= sq[i-2]
    #     power = 1
    #     count += 1
    #     i = 1

    # res = set()
    # res.add(count)
    
    # count = 0
    # # 1, 4 빼고 확인
    # for i in range(len(sq) - 1):
    #     for j in range(len(sq) - 1):
    #         if n - sq[i] - sq[j] == 0:
    #             res.add(2)
    #             break

    # for i in range(len(sq) - 1):
    #     for j in range(len(sq) - 1):
    #         for k in range(len(sq) - 1):
    #             if n - sq[i] - sq[j] - sq[k] == 0:
    #                 res.add(3)
    #                 break

    # print(min(min(res), 4))

