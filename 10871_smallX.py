def smallNum(n, lst, x):
    smallX = []
    for i in range(n):
        if lst[i] < x:
            smallX.append(str(lst[i]))

    return smallX

if __name__ == "__main__":
    nx = input()
    numbers = input()

    lstnx = nx.split(" ")
    N = int(lstnx[0])
    X = int(lstnx[1])
    slst = numbers.split(" ")
    # number of elements of nlst and n should match
    if len(slst) == N:
        nlst = list(map(int, slst))
        # print(nlst)
        smallerX = smallNum(N, nlst, X)
        strSmallerX = " ".join(smallerX)
        print(strSmallerX)