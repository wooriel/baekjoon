# 순열 nPr = n!/(n-r)! (순서 상관 유)
# 조합 nCr = n!/(n-r)!r! (순서 상관 무)

# 전체 경우의 수 = nCm
# k를 뽑는 경우의 수 = mCk (nCk가 아님)

def comb(n, k):
    numer = 1
    denom = 1
    while k > 0:
        numer *= n
        n -= 1
        denom *= k
        k -= 1
    return numer/denom

if __name__ == "__main__":
    n, m, k = input().split(" ")
    n = int(n)
    m = int(m)
    k = int(k)

    # k개 뿐만 아니라 k+1 ... m개를 포함하는 경우까지 다 더해주어야 한다
    total_prob = 0
    while m >= k:
        if n-m < m-k:
            total_prob = 1
            break
        else:
            prob = comb(m, k) * comb(n-m, m-k) / comb(n, m)
            total_prob += prob
            k += 1

    print(total_prob)
        