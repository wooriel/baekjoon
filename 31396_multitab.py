# -*- coding: utf-8 -*-
from sys import stdin
from collections import defaultdict

if __name__ == "__main__":
    ntab, nroot, nelect = map(int, stdin.readline().split())
    tabs = list(map(int, stdin.readline().split()))
    tabs.sort()

    elects = list(map(int, stdin.readline().split()))
    delect = defaultdict(int) # dictionary of electronic devices
    total = 0
    elects.sort()
    for elem in elects:
        total += elem
        delect[elem] += 1

    lvl = 0 # current level
    nmult = 0
    avail = nroot
    navail = 0
    count = 0

    lvls = list(set(elects))
    lvls.sort(reverse=True)
    nlvl = lvls.pop() # 0 이상인 다음 레벨
    if len(lvls) != 0 and nlvl == 0:
        nlvl = lvls.pop()
    nelect = delect[nlvl]

    opt_lvl = 0
    
    while total > 0 and len(tabs) > 0:
        if avail > nmult:
            cur_mult = tabs.pop()
            nmult += 1
            navail += cur_mult
        else:
            # update count and avail
            if avail - nmult < delect[lvl]:
                count += avail - nmult
                if opt_lvl != lvl:
                    delect[lvl]  
                avail = navail
            else: # avail - nmult > delect[lvl]
                count += delect[lvl]
                avail = navail + (avail - nmult - delect[lvl])
            total -= delect[lvl] # count와는 다름

            # update lvl, navail, nmult
            lvl = nlvl
            if len(lvls) != 0:
                nlvl = lvls.pop()
            navail = 0

            nmult = 0
    if avail - nmult < delect[lvl]:
        count += avail - nmult
    else: # avail - nmult > delect[lvl]
        count += delect[lvl]
        avail = navail + (avail - nmult - delect[lvl])
    total -= delect[lvl]

    lvl += 1
    if len(tabs) == 0:
        while total > 0 and avail > 0:
            avail -= delect[lvl]
            count += delect[lvl]
            total -= delect[lvl]
            lvl += 1
            
    print(count)