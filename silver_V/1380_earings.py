# 귀걸이 압수당한 여학생 수
# n줄에 걸친 여학생들의 이름 성
# 2n-1줄에 걸쳐 여학생 번호와 A 혹은 B

# 귀걸이 못 돌려받은 학생 이름 성

if __name__ == "__main__":
    # gstd_num = int(input())
    outputs = []
    scenario = 0
    while True:
        gstd_num = int(input())
        if gstd_num == 0:
            break
        gstd_lst = []
        for i in range(gstd_num):
            gstd_lst.append(input())
        # 번호만 2번 나오는지 보면 됨
        idxes = []
        for j in range(gstd_num*2 - 1):
            stridx = input().split(' ')[0]
            if stridx not in idxes:
                idxes.append(stridx)
            else:
                idxes.remove(stridx)
        no_earng_idx = int(idxes[0])
        std_name = gstd_lst[no_earng_idx - 1]
        scenario += 1
        output = "{} {}".format(scenario, std_name)
        outputs.append(output)
        

    for output in outputs:
        print(output)