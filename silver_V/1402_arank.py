def get_a(n, _n):
    if n - _n > 0:
        if abs(n - _n) % 2 == 0:
            return 1
        else:
            # 1을 더해주면 된다
            if (abs(n - _n) + 1) % 2 == 0:
                return 1
    else:
        return 1
    
    return 1

if __name__ == "__main__":
    num_test = int(input())
    for i in range(num_test):
        # print('yes') 이걸 내도 맞긴 함.....
        a, _a = map(int, input().split(" "))
        if a == _a:
            print("yes")
        else:
            if get_a(a, _a) == 1:
                print("yes")