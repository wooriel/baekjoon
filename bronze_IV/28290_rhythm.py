# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    _str = stdin.readline().rstrip()

    if _str == "fdsajkl;" or _str == "jkl;fdsa":
        print("in-out")
    elif _str == "asdf;lkj" or _str == ";lkjasdf":
        print("out-in")
    elif _str == "asdfjkl;":
        print("stairs")
    elif _str == ";lkjfdsa":
        print("reverse")
    else:
        print("molu")
