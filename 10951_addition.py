def addition(a, b):
    return a+b

if __name__ == "__main__":
    aandb = "."
    res = []
    while True:
        try:
            aandb = input()
            lst = aandb.split(" ")
            res.append(addition(int(lst[0]), int(lst[1])))
        except EOFError:
            break   
    
    for elem in res:
        print(elem)
    
# to trigger EOFError on Windows: Ctrl+Z
# to trigger EOFError on Windows: Ctrl+Ds