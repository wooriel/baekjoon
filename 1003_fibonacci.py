# -*- coding:utf-8 -*-

def count_0_1(n):
    a = 1
    b = 2
    count_a = [0, 1]
    count_b = [1, 1]
    if n == a:
        return count_a
    elif n == b:
        return count_b
    else:
        while b != n:
            count_c = [count_a[0] + count_b[0], count_a[1] + count_b[1]]
            count_a = count_b
            count_b = count_c
            a += 1
            b += 1
        return count_b

if __name__ == "__main__":
    case = int(input())
    nums = []
    for i in range(case):
        nums.append(int(input()))

    for num in nums:
        if num == 0:
            print("1 0")
        else:
            print("{} {}".format(count_0_1(num)[0], count_0_1(num)[1]) )
