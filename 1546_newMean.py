def newMean(n, lst):
    sum = 0
    max = int(lst[0])
    for elem in lst:
        ielem = int(elem)
        sum += ielem
        if max < ielem:
            max = ielem
    return sum / len(lst) / max * 100

if __name__ == "__main__":
    nscore = input()
    scores = input()
    strscrlst = scores.split(" ")
    print(newMean(int(nscore), strscrlst))