# -*- coding: utf-8 -*-

if __name__ == "__main__":
    scale = list(map(int, input().split()))

    dir = ""
    for i in range(len(scale)-1):
        cur_dir = "descending"
        if scale[i] < scale[i+1]:
            cur_dir = "ascending"
        if dir == "":
            dir = cur_dir
        else:
            if dir != cur_dir:
                dir = "mixed"
                break

    print(dir)