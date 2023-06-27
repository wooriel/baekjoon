def z_range(log2_w, r, c):
    w = pow(2, log2_w)
    # total_tiles = pow(w, 2)
    numtiles = 0
    while w != 1:
        # 사분할
        w = w>>1
        if r < w and c < w:
            pass
            # nothing is added to the numtiles
            # r and c does not change
        elif r < w and c >= w:
            # 1/4 of the total tiles (w^2) is added to the numtiles
            numtiles += pow(w, 2)
            # if c == w:
            c -= w
            # else:
            #     c = c>>1
        elif r >= w and c < w:
            # half of the total tiles are added to the numtiles
            numtiles += pow(w, 2) * 2
            # if r == w:
            r -= w
            # else:
            #     r = r>>1
        else:
            # 3/4 of the total tlies are added to the numtiles
            numtiles += pow(w, 2) * 3
            # if r == w:
            r -= w
            # if c == w:
            c -= w
            # r = r>>1
            # c = c>>1
    # # handle differently for w == 2
    # w = w>>1
    # if r <= w and c <= w:
    #     pass
    # elif r > w and c <= w:
    #     numtiles += pow(w, 2)
    #     r = r % 2
    # elif r <= w and c > w:
    #     numtiles += pow(w, 2) * 2
    #     c = c % 2
    # else:
    #     numtiles += pow(w, 2) * 3
    #     r = r % 2
    #     c = c % 2
    # w>>1
    # if r <= half and c <= half:
    #     pass
    # elif r > half and c <= half:
    #     numtiles += pow(w, 2)
    # elif r <= half and c > half:
    #     numtiles += pow(w, 2) * 2
    # else:
    #     numtiles += pow(w, 2) * 3
    return numtiles

if __name__ == "__main__":
    log2_w, r, c = map(int, input().split())
    print(z_range(log2_w, r, c))