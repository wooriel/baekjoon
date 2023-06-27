

def exists(tup, trees):
    for i in range(len(trees)):
        if tup in trees[i]:
            return 1
    return 0


def build_tree(cur, w, h, case, tset=set()):
    """_summary_

    Args:
        cur (_type_): _description_
        w (_type_): _description_
        h (_type_): _description_
        block (_type_): _description_
        tset (_type_, optional): _description_. Defaults to set().

    Returns:
        tset: _description_
    """
    if cur not in case or cur[0] > w or cur[1] > h:
        return 
    else:
        tset.add(cur)
        build_tree((cur[0] + 1, cur[1]), w, h, case, tset)
        build_tree((cur[0], cur[1] + 1), w, h, case, tset)
    return tset

if __name__ == "__main__":
    test_cases = int(input())

    num_cabbage = []
    for i in range(test_cases):
        # input rectangle_cabbage(rc) = width, height, num_cabbage
        rc = list(map(int, input().split()))
        case = []
        # input cases
        for j in range(rc[2]):
            case.append(tuple(map(int, input().split())))

        trees = []
        for elem in case:
            # check for existance
            if exists(elem, trees) == 0:
                tree = build_tree(elem, rc[0], rc[1], case, set())
                trees.append(tree)

        num_cabbage.append(len(trees))

    for i in range(len(num_cabbage)):
        print(num_cabbage[i])