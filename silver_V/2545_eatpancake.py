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

if __name__ == "__main__":
    cases = int(input())
    _ = input()

    max_sizes = []
    for i in range(cases):
        w, d, h, t = map(int, input().split(" "))
        for j in range(t):
            w, d, h = max_minus1(w, d, h)
        if i != cases-1:
            _ = input()
        max_sizes.append(w*d*h)

    for k in range(len(max_sizes)):
        print(max_sizes[k])