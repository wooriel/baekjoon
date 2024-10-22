# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    inp = stdin.readline().rstrip()
    count = 1
    while True:
        if inp == '0':
            break
        else:
            _l = len(inp)
            if _l % 2 == 1:
                print('Test {}: {}'.format(count, inp))
                count += 1
                inp = stdin.readline().rstrip()
            else:
                ninp = []
                for i in range(0, _l, 2):
                    for j in range(int(inp[i])):
                        ninp.append(str(inp[i+1]))
                _ninp = ''.join(ninp)
                if _ninp == inp:
                    print('Test {}: {}'.format(count, inp))
                    count += 1
                    inp = stdin.readline().rstrip()
                else:
                    inp = _ninp
