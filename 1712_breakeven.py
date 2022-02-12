def breakeven(fixed, gen, sell):
    benefit = sell - gen
    if benefit <= 0:
        return -1
    breakevenpt = fixed//benefit + 1
    # even the remainder: fixed % benefit is 0, add 1 more computer
    # there should be profit, we are not getting the point of selling cost being equal to making cost     
    # print("Cost for making {0} computers: {1}".format(breakevenpt, fixed + gen*breakevenpt))
    # print("Cost for selling {0} computers: {1}".format(breakevenpt, sell*breakevenpt))
    return breakevenpt

if __name__ == "__main__":
    comp = input()
    lst = comp.split(" ")
    print(breakeven(int(lst[0]), int(lst[1]), int(lst[2])))