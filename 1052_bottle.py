def lst_count(lst, k):
    lst = [int(x) for x in lst]
    idx = 0
    for i in range(len(lst)):
        if lst[i] == 1:
            k -= 1
        if k == 0:
            idx = i-1
            break
    sublst = lst[:idx:-1]

    to_subtract = 0
    # converts back into 10digit num
    for j in range(len(sublst)):
        if sublst[j] == 1:
            to_subtract += pow(2, j) * sublst[j]

    # print(to_subtract)
    # print(pow(2, len(sublst)))
    num_buy = pow(2,len(sublst)) - to_subtract
    return num_buy

def bottle_num(num_b, k, water):
    while True:
        if bin(num_b).count("1") <= k:
            return water
        else:
            num_b += 1
            water += 1


if __name__ == "__main__":
    num_b, k = map(int, input().split())
    print(bottle_num(num_b, k, 0))
    # if num_b <= k:
    #     print(0)
    # else:
        # bin_num = bin(num_b)
        # print(lst_count(list(str(bin_num)[2:]), k))
        # print(lst_count([0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,1,1,1,1], 5))
        # print(lst_count([1,1,1,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0], 5))