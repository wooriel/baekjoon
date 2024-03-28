T = int(input())

arr = []
for _ in range(T):

    sum = 0
    input()
    N = int(input())
    sum = 0
    for _ in range(N):
        a = int(input())
        sum += a

    result = sum % N
    arr.append(result)
    if _ != T - 1:
        print()

for i in range(len(arr)):
    if arr[i] == 0:
        print('YES')
    else:
        print('NO')