# -*- coding: utf-8 -*-

if __name__ == "__main__":
    cases = int(input())

    wave = [1, 1, 1]
    for i in range(cases):
        inp = int(input())
        for j in range(inp - len(wave)):
            wave.append(wave[-2] + wave[-3])
        print(wave[inp-1])

