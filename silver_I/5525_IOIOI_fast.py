# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    pn = int(stdin.readline())

    slen = int(stdin.readline())
    sio = stdin.readline().rstrip()
    
    
    if pn > slen // 2:
        print(0)
    else:
        cur = 'I'
        count = 0
        total = 0
        for i in range(slen):
            if sio[i] == cur:
                if cur == 'I':
                    cur = 'O'
                else:
                    cur = 'I'
                count += 1
            else:
                if sio[i] == 'O':
                    count -= 1
                else: # sio[i] == 'I', cur == 'O'
                    cur = 'I'
                n = count // 2
                count = 0
                if n >= pn:
                    total += n - pn + 1

                # save current data
                if sio[i] == cur:
                    cur = 'O'
                    count += 1

        # 마지막줄 처리
        if count > 0:
            # 1, 3, IIO -> 0 (without below, 1)
            if slen >= 1:
                if sio[slen-1] == 'O':
                    count -= 1
            n = count // 2
            count = 0
            if n >= pn:
                total += n - pn + 1

        print(total)
