def get_num(n):
    length = len(str(n))
    res = 0
    for i in range(length):
        dig = n%10
        n = n//10

        if dig > 4:
            res += (dig-1) * pow(9, i)
        else:
            res += dig * pow(9, i)

    return res

if __name__ == "__main__":
    num = int(input())
    res = get_num(num)

    print(res)