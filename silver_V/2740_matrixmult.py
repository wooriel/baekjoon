if __name__ == "__main__":
    # 행렬 A의 크기 n(height)*m(width)
    n, m = input().split()
    n = int(n)
    m = int(m)

    A = []
    # nested loop 쓰는거 아님
    for i in range(n):
        row = input().split()
        A.append(row)

    m, k = input().split()
    m = int(m)
    k = int(k)
    
    B = []
    for i in range(m):
        row = input().split()
        B.append(row)

    # B는 transpose시킬거다. 원활한 곱셈을 위해 <- 아 귀찮
    # C = []
    for i in range(n):
        row = []
        for j in range(k):
            elem = 0
            for c in range(m):
                elem += int(A[i][c]) * int(B[c][j])
            row.append(str(elem))
        print(" ".join(row))
        # C.append(row)