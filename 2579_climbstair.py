

# 3칸 뛰는것, 또는 3칸 연속 밟기 안됨.
# 10 20 15 | 10 (시작점 정하기) - 2칸앞 즉 3번째 스킵이 좋은데 2번째 스킵해서 합이 더 좋으면 업데이트
# 20 15 25 | 15
# 15 25 10 | 10
# 25 10 20 | 10

if __name__ == "__main__":
    num_stairs = int(input())
    scores = []

    for i in range(num_stairs):
        list.append(int(input()))

    