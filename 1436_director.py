def getN666(n):
    set666 = {'666'}
    # check if the length if bigger than n
    while len(set666) < n:
        # exclude '0...0666': always located front -> actually no need to
        set666 = make666set(set666)
    # make the list into ascending order
    lst666 = list(set666)
    lst666.sort()
    return int(lst666[n-1])


def make666set(prevset):
    newlst = []
    # convert into list
    prevlst = list(prevset)
    for elem in prevlst:
        for i in range(0, 10):
            front  = '{0}{1}'.format(str(i), elem)
            newlst.append(front)
            back = '{0}{1}'.format(elem, str(i))
            newlst.append(back)
    return set(newlst)
    


if __name__ == "__main__":
    N = int(input())
    ans = getN666(N)
    print(ans)
    # newset = make666set({'666'})
    # # print(newset)
    # nlst = list(newset)
    # nlst.sort()
    # # print(nlst)
    # print(len(nlst))

    # newset2 = make666set(newset)
    # nlst2 = list(newset2)
    # nlst2.sort()
    # # print(nlst2)
    # print(len(nlst2))

    # newset3 = make666set(newset2)
    # nlst3 = list(newset3)
    # nlst3.sort()
    # # print(nlst3)
    # print(len(nlst3))

   


# _ one digit
# 0-5일때는 666이 뒤에 오는게 좋다
# 6661-6669가 사이에 들어간다
# 6일때는 순서를 무시 (6666)
# 7-9일때는 666이 앞에 오는게 좋다

# _ _ two digit
# 66666의 경우...

# 1 : 0666
# 2 : 1666
# 6 : 5666

# 7 : 6660
# 13 : 6666 (겹침)
# 16 : 6669

# 17 : 7666
# 19 : 9666

# 앞이 00인 경우 제외
# 21 - 1 : 10666
# 22 - 1 : 11666
# 26 - 1 : 15666

# 27 - 1 : 16660
# 28 - 1 : 16661
# 33 - 1 : 16666 (겹침)
# 36 - 1 : 16669

# 37 - 1 : 17666
# 39 - 1 : 19666

# 0
# 1-9
# 10-19
# 20-29

# 60-69

# _ = 10 * 2 - 1 (6인경우)

# 50
# (9 * 10 + 1 = 91) * 2 + 10*10 -  (6인경우)
# _ _