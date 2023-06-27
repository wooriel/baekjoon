def check_alp(alp: str, alp2: str):
    # returns interval between number
    alps = ["A", "B", "C", "D", "E", "F"]
    idx1 = alps.index(alp)
    idx2 = alps.index(alp2)
    if abs(idx2 - idx1) == 1:
        return 1
    elif abs(idx2 - idx1) == 2:
        return 2
    else:
        return -1 # invalid
    
# 첫번째 조건에 연속해서 쓰려다가 그냥 두개의 interval 합만 맞는지 보고 nested condition 줄일 생각
# def check_num(num: int, num2: int, interval: int):
#     if abs(num2 - num) == interval:
#         return 1
#     else:
#         return -1

def check_num(num:int, num2: int):
    if abs(num2 - num) == 1:
        return 1
    elif abs(num2 - num) == 2:
        return 2
    else:
        return -1

if __name__ == "__main__":
    n = 36

    # knight가 갈 수 있는곳인지 확인
    # 마지막에서 A1로 올 수 있는지 확인

    path_set = set()

    # "A1" 이 항상 시작임 <- 아님
    # 미리 다 입력을 받고 처리해야함 <- 이건 아닌데 입력이 남은 상태에서 프린트는 ㄴㄴ
    # 어이없게도 capital 까먹어서 틀림 ㅋㅋㅋ
    start_word = input()
    prev_word = start_word
    path_set.add(prev_word)
    to_print = "Valid"
    for k in range(1, n):
        cur_word = input()
        path_set.add(cur_word)
        alp_res = check_alp(prev_word[0], cur_word[0])
        num_res = check_num(int(prev_word[1]), int(cur_word[1]))
        if alp_res + num_res != 3:
            to_print = "Invalid"
            # break

        prev_word = cur_word

    # prev_word에 가장 마지막 element가 저장되어있음
    interval_sum = check_alp(prev_word[0], start_word[0]) + check_num(int(prev_word[1]), int(start_word[1]))
    if interval_sum != 3:
        to_print = "Invalid"
    else:
        # 중복있는지 확인
        if len(list(path_set)) != n:
            to_print = "Invalid"

    print(to_print)