def countCrotia(crotias, cset):
    # c=c-dz=
    count = 0
    index = 0
    while index < len(crotias):
        endIndex = index + 2
        if endIndex > len(crotias):
            endIndex = -1
        crotia = crotias[index:endIndex]
        if crotia in cset:
            index += 2
            count += 1
        else:
            endIndex += 1
            crotia = crotias[index:endIndex]
            if crotia in cset:
                index += 3
                count += 1
            else: # normal alphabet
                index += 1
                count += 1

    return count
        


if __name__ == "__main__":
    string = input()
    crotiaCharacters = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="}
    # crotiaCharlst = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    print(countCrotia(string, crotiaCharacters))