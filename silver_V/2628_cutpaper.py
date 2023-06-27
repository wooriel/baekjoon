
# 안됨 범위에 포함안되는데 간격이 넒은거 있을수도
# def cut(cut, s, e):
#     if e - cut > cut - s:
#         return cut, e
#     else:
#         return s, cut

def max_len(lst):
    max_len = 0
    for i in range(len(lst)-1):
        length = lst[i+1] - lst[i]
        if max_len < length:
            max_len = length

    return max_len
    

if __name__ == "__main__":
    w, h = input().split()
    # s_w, s_h = 0, 0
    e_w = int(w)
    e_h = int(h)

    num_cut = int(input())
    w_cuts = [0]
    h_cuts = [0]
    for i in range(num_cut):
        flag, idx = input().split()
        cut_idx = int(idx)
        if flag == '1':
            w_cuts.append(cut_idx)
        else: # flag == '0'
            h_cuts.append(cut_idx)
    w_cuts.append(e_w)
    h_cuts.append(e_h)

    # 정렬해야함
    w_cuts.sort()
    h_cuts.sort()

    max_w = max_len(w_cuts)
    max_h = max_len(h_cuts)

    print(max_w * max_h)
