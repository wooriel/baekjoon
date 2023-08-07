def adj_mastermind(ans, guess):
    colors = [0, 0, 0] # white gray black
    used = [] # saved (idx of guess, color) of guess
    for i in range(len(ans)):
        prev_colors = colors.copy()
        if ans[i] == guess[i]:
            used, colors = check_idx(used, colors, i, 2) # 2 represents black
        elif i != 0 and ans[i] == guess[i-1]:
            used, colors = check_idx(used, colors, i-1, 1) # 1 represents grey
            if prev_colors == colors:
                if i != 0 and ans[i] == guess[i+1]:
                    used, colors = check_idx(used, colors, i+1, 1) # 1 represents grey
                    if prev_colors != colors:
                        break
                break
        elif i != len(ans) - 1 and ans[i] == guess[i+1]:
            used, colors = check_idx(used, colors, i+1, 1) # 1 represents grey
            if prev_colors == colors:
                if i != 0 and ans[i] == guess[i-1]:
                    used, colors = check_idx(used, colors, i-1, 1) # 1 represents grey
                    if prev_colors != colors:
                        break
                break
        else:
            for j in range(len(guess)):
                if j != i and j != i-1 and j != i+1 and ans[i] == guess[j]:
                    # prev_colors = colors.copy()
                    used, colors = check_idx(used, colors, j, 0) # 0 represents white
                    # color에 변화가 없으면 멈추면 안됨
                    if prev_colors != colors:
                        break

    return colors


def check_idx(used_lst:list, colors:list, idx, color:int):
    # ex) ABABAA BCBCAA 같은 경우를 보면 왼쪽의 A가 오른쪽과 비교해서 white에 더해짐
    # 근데 5번째 A를 비교할때 A가 사실상 black으로 들어가야함. 이런 경우를 잡아주기 위해서 만들었다.

    # 기존의 guess index가 어떤 색에 더해졌는지를 보고 새롭게 더할 색이 더 강하면 바꾸어주는 역할
    # guess index와 color은 새로 더하려는 컬러

    for i in range(len(used_lst)):
        if used_lst[i][0] == idx:
            if used_lst[i][1] < color:
                # return the color 1을 빼야하는 기존의 컬러
                colors[used_lst[i][1]] -= 1
                colors[color] += 1
                # change the list
                used_lst[i][1] = color

                return used_lst, colors
            elif used_lst[i][1] == color:
                return used_lst, colors
        
    # 겹치는 index가 없을때
    used_lst.append([idx, color])
    colors[color] += 1

    return used_lst, colors
    


# def comp_color(col1, col2):
#     if col1 >= col2:
#         return -1
#     else:
#         return 1

def print_ans(guess, colors:list):
    return "{}: {} black, {} grey, {} white".format(guess, colors[2], colors[1], colors[0])

if __name__ == "__main__":
    inp = []
    to_print = []
    while len(inp) != 1:
        inp = input().split(" ")
        if inp[0] == '#':
            break
        colors = adj_mastermind(inp[0], inp[1])
        to_print.append(print_ans(inp[1], colors))

    for i in range(len(to_print)):
        print(to_print[i])