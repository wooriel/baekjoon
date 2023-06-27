def mul5(n):
    num5 = 0
    while n % 5 == 0:
        n = n // 5
        num5 += 1
    return num5


def mul2(n):
    num2 = 0
    while n % 2 == 0:
        n = n // 2
        num2 += 1
    return num2

def count0(n):
    num2 = 0
    num5 = 0
    for i in range(1, n + 1):
        if i % 5 == 0:
            num5 += mul5(i)
        if i % 2 == 0:
            num2 += mul2(i)
    return min(num2, num5)


if __name__ == "__main__":
    n = int(input())
    num0 = count0(n)
    print(num0)