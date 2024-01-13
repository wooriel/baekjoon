
n = 22
group_num = [1, 1, 2, 3, 3, 3, 4, 5]

if len(group_num) <= 2:
        print(-1)
else:
    if len(group_num) != 3:
        low_gp = 0
        low_gp2 = 0
        i = 0
        while low_gp2 < n/3 and i < len(group_num) - 2:
            low_gp2 += group_num[i]
            i += 1
        low_gp = low_gp2 - group_num[i-1]
        mid_gp = 0
        mid_gp2 = 0
        mid_gp2_1 = 0
        mid_gp2_2 = 0
        j1 = i-1 # log_gp related index
        j2 = i # log_gp2 related index
        while mid_gp2 < n/3 and j1 < len(group_num) - 1:
            mid_gp2 += group_num[j1]
            j1 += 1
        mid_gp = mid_gp2 - group_num[j1-1]
        while mid_gp2_2 < n/3 and j2 < len(group_num) - 1:
            mid_gp2_2 += group_num[j2]
            j2 += 1
        mid_gp2_1 = mid_gp2_2 - group_num[j2-1]
        mins = []
        if low_gp != 0 and mid_gp != 0:
            min_num1 = max(abs(low_gp - mid_gp), abs(2*low_gp - n + mid_gp), abs(2*mid_gp - n + low_gp))
            mins.append(min_num1)
        if low_gp != 0 and mid_gp2 != 0:
            min_num2 = max(abs(low_gp - mid_gp2), abs(2*low_gp - n + mid_gp2), abs(2*mid_gp2 - n + low_gp))
            mins.append(min_num2)
        if low_gp2 != 0 and mid_gp2_1 != 0:
            min_num3 = max(abs(low_gp2 - mid_gp2_1), abs(2*low_gp2 - n + mid_gp2_1), abs(2*mid_gp2_1 - n + low_gp2))
            mins.append(min_num3)
        if low_gp2 != 0 and mid_gp2_2 != 0:
            min_num4 = max(abs(low_gp2 - mid_gp2_2), abs(2*low_gp2 - n + mid_gp2_2), abs(2*low_gp2 - n + mid_gp2_2))
            mins.append(min_num4)
        print(min(mins))
        
        # low_gp = 0
        # min_num = n
        # for i in range(len(group_num) - 2):
        #     low_gp += group_num[i]
        #     mid_gp = 0
        #     for j in range(i + 1, len(group_num) - 1):
        #         mid_gp += group_num[j]
        #         # calculate min
        #         num = max(abs(low_gp - mid_gp), abs(2*low_gp - n + mid_gp), abs(2*mid_gp - n + low_gp)) 
        #         if min_num > num:
        #             min_num = num
        #             if min_num == 0:
        #                 break
        #     if min_num == 0:
        #             break
        # print(min_num)
    else:
        print(max(abs(group_num[0] - group_num[1]), abs(group_num[0] - group_num[2]), abs(group_num[1] - group_num[2])))