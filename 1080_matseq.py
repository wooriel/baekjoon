def find_costs(a, b):

    to_visit = [0, 0]
    min_cost = 2500
    for i in range():
        for j in range():
            # center = a[i][j]
            cur_cost = difference(a, b, i, j)
            if min_cost > cur_cost:
                min_cost == cur_cost
                to_visit[0] = i
                to_visit[1] = j
    

def difference(a, b, m, n):
    # 해당 인덱스만 뒤집었을때 다른 정도(cost)를 리턴한다.
    cost = 0
    for i in range(a):
        for j in range(a[i]):
            if (i == m-1 or i == m or i == m+1) and (j == n-1 or j == n or j == n+1):
                cost += opposite(a, i, j) == b[i][j]
            cost += a[i][j] == b[i][j]
    return cost

def cost(a, b, m, n):
    cost = 0
    if m > 0 and n > 0:
        # a[m-1][n-1] = opposite(a, m-1, n-1)
        # cost += a[m-1][n-1] == b[m-1][n-1]
        cost += opposite(a, m-1, n-1) == b[m-1][n-1]
    if m > 0:
        # a[m-1][n] = opposite(a, m-1, n)
        # cost += a[m-1][n] == b[m-1][n]
        cost += opposite(a, m-1, n) == b[m-1][n]
    if m > 0 and n < len(a[m]) - 1:
        # a[m-1][n+1] = opposite(a, m-1, n+1)
        # cost += a[m-1][n+1] == b[m-1][n+1]
        cost += opposite(a, m-1, n+1) == b[m-1][n+1]
    if n > 0:
        # a[m][n-1] = opposite(a, m, n-1)
        # cost += a[m][n-1] == b[m][n-1]
        cost += opposite(a, m, n-1) == b[m][n-1]
    # a[m][n] = opposite(a, m, n)
    # cost += a[m][n] == b[m][n]
    cost += opposite(a, m, n) == b[m][n]
    if n < len(a[m]) - 1:
        # a[m][n+1] = opposite(a, m, n+1)
        # cost += a[m][n+1] == b[m][n+1]
        cost += opposite(a, m, n+1) == b[m][n+1]
    if m < len(a) - 1 and n > 0:
        # a[m+1][n-1] = opposite(a, m+1, n-1)
        # cost += a[m+1][n-1] == b[m+1][n-1]
        cost += opposite(a, m+1, n-1) == b[m+1][n-1]
    if m < len(a) - 1:
        # a[m+1][n] = opposite(a, m+1, n)
        # cost += a[m+1][n] == b[m+1][n]
        cost += opposite(a, m+1, n) == b[m+1][n]
    if m < len(a) - 1 and n < len(a[m]) - 1:
        # a[m+1][n+1] = opposite(a, m+1, n+1)
        # cost += a[m+1][n-1] == b[m+1][n-1]
        cost += opposite(a, m+1, n+1) == b[m+1][n-1]

    return cost

def opposite(a, m, n):
    if a[m][n] == '0':
        return '1'
    else:
        return '0'
        


if __name__ == "__main__":
    r, c = map(int, input().split())

    a = []
    b = []
    for i in range(r):
        a.append(list(input()))
    for j in range(r):
        b.append(list(input()))
    # print(a)