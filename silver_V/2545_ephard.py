def max_minus1(x, y, z):
    if x > y:
        if x > z:
            return x-1, y, z
        else:
            return x, y, z-1
    else:
        if y > z:
            return x, y-1, z
        else:
            return x, y, z-1
        

def max_minusT(x, y, z, t):
    min_num = min(min(x, y), z)
    sum = x + y + z
    if t >= sum:
        return 0
    else:
        abs_val = sum - min_num*3

        abs1 = x - min_num
        abs2 = y - min_num
        abs3 = z - min_num
        max_abs = max(max(abs1, abs2), abs3)
        next_abs = abs_val - max_abs
        n_t = t - (max_abs - next_abs)
        if n_t > 0:
            next_abs -= n_t//2
            if n_t % 2 == 1:
                return min_num * (min_num + next_abs) * (min_num + next_abs - 1) # 이걸 +1하고 앉아있었음
            else:
                return min_num * pow(min_num + next_abs, 2) 
        else:
            if max_abs != 0:
                return min_num * (min_num + next_abs) * (min_num + max_abs - t)
            else: # max_abs == 0, all three elements are equal.
                dist = t // 3
                remainder = t % 3
                if remainder == 2:
                    return (min_num - dist) * pow(min_num - dist - 1, 2)
                elif remainder == 1:
                    return pow(min_num - dist, 2) * (min_num - dist - 1)
                else:
                    return pow(min_num - dist, 3)


if __name__ == "__main__":
    # does not work
    cases = int(input())
    _ = input()

    max_sizes = []
    for i in range(cases):
        w, d, h, t = map(int, input().split(" "))
        max_size = max_minusT(w, d, h, t)
        max_sizes.append(max_size)
        if i != cases-1:
            _ = input()

    for k in range(len(max_sizes)):
        print(max_sizes[k])