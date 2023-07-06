# -*- coding: utf-8 -*-
def find_room(r, w, n):
    final = n//r
    if n % r != 0:
        final += 1
    first = n % r
    if first == 0:
        first = r

    room = str(first) + '0'*(len(str(w))-len(str(final))) + str(final)
    if len(str(w)) == 1:
        room = str(first) + '0'*(2-len(str(final))) + str(final)

    return room




if __name__ == "__main__":
    cases = int(input())

    key = []
    for i in range(cases):
        floor, room, nth = map(int, input().split())
        key.append(find_room(floor, room, nth))

    for k in key:
        print(k)
