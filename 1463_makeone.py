def helpone(prevnums, cnt):
    if 1 in prevnums:
        return cnt
    else:
        nnums = []
        for i in range(len(prevnums)):
            pnum = prevnums[i]
            if pnum % 3 == 0:
                nnums.append(pnum//3)
            if pnum % 2 == 0:
                nnums.append(pnum//2)
            nnums.append(pnum-1)
        return helpone(list(set(nnums)), cnt+1)


def makeone(n):
    count = 0
    mincount = 1000000
    initkey = [n]
    res = helpone(initkey, count)
    return res

if __name__ == "__main__":
    num = int(input())
    # print("{0} is {1}".format(num, type(num)))
    print(makeone(num))
