def stringA(n):
    strA = ""
    while n - 4 > 0:
        strA += "AAAA"
        n -= 4
    return strA, n


def stringB(n):
    strB = ""
    while n - 2 > 0:
        strB += "BB"
        n -= 2
    return strB

if __name__ == "__main__":
    polyA = "AAAA"
    polyB = "BB"

    pattern = input()
    pat_lst = pattern.split(".")
    flag = 0
    for i in range(len(pat_lst)):
        n = len(pat_lst[i])
        if n % 2 != 0:
            flag = -1
            break
        else:
            strA, n = stringA(n)
            strB = stringB(n)
            pat_lst[i] = strA + strB
    
    count = 0
    idx = 0
    while count < len(pattern):
        if pattern[count] == 'X':
            next_count = count + len(pat_lst[idx])
            pattern = pattern[:count] + pat_lst[idx] + pattern[next_count:]
            count = next_count
            idx += 1
        else:
            count += 1
