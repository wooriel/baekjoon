# alp = A to Z, 0 for space
# convert into 5-digit binary number

def return_idx(r_idx, c_idx, flag, r_dir, c_dir):
    if flag == 1 and r_dir == 1:
        r_idx += 1
    elif flag == 1 and r_dir == -1:
        r_idx -= 1
    elif flag == -1 and c_dir == 1:
        c_idx += 1
    else: # flag == -1 and c_dir == -1:
        c_idx -= 1

    return r_idx, c_idx


def check_edge(r_idx, c_idx, flag, r_dir, c_dir, r_str, c_str, r_end, c_end):
    # 방향을 트는것
    if r_idx == r_end:
        c_end -= 1
        flag = -1
        r_dir = -1
        r_idx -= 1
        # index 변화
        r_idx, c_idx = return_idx(r_idx, c_idx, flag, r_dir, c_dir)
    elif r_idx == r_str:
        c_str += 1
        flag = -1
        r_dir = 1
        r_idx += 1
        # index 변화
        r_idx, c_idx = return_idx(r_idx, c_idx, flag, r_dir, c_dir)
    elif c_idx == c_end:
        r_str += 1
        flag = 1
        c_dir = -1
        c_idx -= 1
        # index 변화
        r_idx, c_idx = return_idx(r_idx, c_idx, flag, r_dir, c_dir)
    elif c_idx == c_str:
        r_end -= 1
        flag = 1
        c_dir = 1
        c_idx += 1
        # index 변화
        r_idx, c_idx = return_idx(r_idx, c_idx, flag, r_dir, c_dir)
    

    return r_idx, c_idx, flag, r_dir, c_dir, r_str, c_str, r_end, c_end
        

def reorder(r, c, strnum):
    lst = []
    idx = c
    # 소용돌이 matrix 형태로 저장.
    # 다만 nested list는 아니고 column이 문자열인 형태
    for i in range(r):
        if i != r - 1:
            lst.append(strnum[idx-c:idx])
        else:
            lst.append(strnum[idx-c:])
        idx += c

    orig_lst = []
    # 변수들 설정
    r_idx = 0
    c_idx = 0
    flag = -1 # row_order = 1, column_order = -1
    r_dir = 1 # right = 1, left = -1
    c_dir = 1

    r_str = -1
    r_end = r
    c_str = -1
    c_end = c
    while len(orig_lst) != len(strnum):
        orig_lst.append(lst[r_idx][c_idx])
        # if flag == 1:
        #     return_r_idx
        # else:
        #     return_c_idx
        r_idx, c_idx = return_idx(r_idx, c_idx, flag, r_dir, c_dir)
    
        r_idx, c_idx, flag, r_dir, c_dir, r_str, c_str, r_end, c_end = check_edge(r_idx, c_idx, flag, r_dir, c_dir, r_str, c_str, r_end, c_end)

    # join the orig_lst into correct order strnum
    return "".join(orig_lst)


def conv_strbin_to_int(digit5, n=5):
    # 5자리 binary 수 -> 정수
    sum = 0
    to_add = 1
    for i in reversed(range(n)):
        if digit5[i] == '1':
            sum += to_add
        to_add = to_add << 1

    return sum


def conv_int_to_char(num):
    # 정수 -> 대문자 및 공백
    # (ascii code에서 대문자 A가 65여서 모든 알파벳 수에다 64 더해주는것.)
    if num == 0:
        return " "
    else:
        return chr(num + 64)
    

def conv_ascii(orig_str: str, n = 5):
    # 소용돌이를 풀어둔 binary 형태의 문자열 -> 메시지로 변환
    count = n
    res_str = []
    while len(orig_str) > count:
        # single underscore: inner argument (not used in outside)
        _int = conv_strbin_to_int(orig_str[count-n:count])
        _char = conv_int_to_char(_int)
        count += n
        
        res_str.append(_char)

    if count == len(orig_str):
        l_int = conv_strbin_to_int(orig_str[count-n:])
        l_char = conv_int_to_char(l_int)
        res_str.append(l_char)

    return "".join(res_str)

def trim_end(res_str: str):
    # 메시지의 공백을 삭제하는 함수
    cut_idx = -1
    for i in range(len(res_str)-1, 0, -1):
        if res_str[i] != " ":
            break
        else:
            cut_idx = i

    if cut_idx == -1:
        return res_str
    else:
        return res_str[:cut_idx]


if __name__ == "__main__":
    # test case t
    num = int(input())

    msg_lst = []
    
    for i in range(num):
        r, c, str_num = input().split()
        r = int(r)
        c = int(c)
        orig_str = reorder(r, c, str_num) # 이진수로 된 문자열 string
        message = conv_ascii(orig_str) # 원래 문자열 리스트
        trimmed = trim_end(message)
        msg_lst.append(trimmed)

    for msg in msg_lst:
        print(msg)