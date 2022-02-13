def check_divisor(num):
    isPrime = True
    if num == 1:
        isPrime = False
        return isPrime
    for i in range(2, num):
        if num % i == 0:
            isPrime = False
            break

    return isPrime


if __name__ == "__main__":
    m = int(input())
    n = int(input())
    primeSum = 0
    primeMin = n+1
    for j in range(m, n+1):
        res = check_divisor(j)
        if res:
            if j < primeMin:
                primeMin = j
            primeSum += j

    if primeSum == 0:
        print(-1)
    else:
        print(primeSum)
        print(primeMin)