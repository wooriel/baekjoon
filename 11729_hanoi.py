def help_hanoi(n, lst, turn):
    if n == 0:
        midstr = '{} {}'.format(turn[0], turn[1])
        # lst.append(midstr)
        print(midstr)
        return
    else:
        another = list({1, 2, 3} - set(turn))
        llst = [turn[0], another[0]]
        lstr = '{} {}'.format(turn[0], another[0])

        help_hanoi(n-1, lst, llst)

        midstr = '{} {}'.format(turn[0], turn[1])
        # lst.append(midstr)
        print(midstr)
        
        rlst = [another[0], turn[1]]
        rstr = '{} {}'.format(another[0], turn[1])
        help_hanoi(n-1, lst, rlst)


def getK(n, k):
    if n == 0:
        return k
    else:
        return getK(n-1, 2*k+1)


if __name__ == "__main__":
    n = int(input())
    print(getK(n, 0))
    order = []
    help_hanoi(n-1, order, [1, 3])
    # print(len(order))
    # for i in range(len(order)):
    #     print(order[i])
    
# 1 3
# 1 2
# 3 2

# 1 3

# 2 1
# 2 3
# 1 3

# n = 1
# k = 1
# 1 3,1

# n = 2
# k = 3
# 1 2,1
# 1 3,2
# 2 3,1

# n = 3
# k = 7
# 1 3.1
# 1 2.|2
# 3 2.1
# 1 3 - 3|3
# 2 1.1
# 2 3.|2
# 1 3.1

# 1
# 1 3
# 3 2
# 2 1
# 1 3

# n = 4
# k = 15 (predict)
# 1 2.1
# 1 3.|2
# 2 3.1

# 1 2 - 3 (dest 1 2)|

# 3 1.1
# 3 2.|2
# 1 2.1

# 1 3 - 4 (dest 1 3)|

# 2 3.1
# 2 1.|2
# 3 1.1

# 2 3 - 3 (dest 2 3)|

# 1 2.1
# 1 3.|2
# 2 3.1