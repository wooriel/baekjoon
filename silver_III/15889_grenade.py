# -*- coding: utf-8 -*-
from sys import stdin

if __name__ == "__main__":
    n = int(stdin.readline())
    dist_ppl = list(map(int, stdin.readline().split()))
    # dist_ppl.sort()
    if n > 1:
        dist_thr = list(map(int, stdin.readline().split()))
        dist_thr.append(0)

        dist = [(dist_ppl[i], dist_thr[i]) for i in range(n)]
        dist.sort()

        dist_ppl = [dist[i][0] for i in range(n)]
        dist_thr = [dist[i][1] for i in range(n)]

        idx_ppl, idx_thr = 1, 0
        idx_pprev = 0
        prev_avail = False

        # check all people
        everyone = True
        rem = []
        for i in range(1, n):
            if dist_ppl[i] - dist_ppl[i-1] > dist_thr[i-1]:
                everyone = False
                rem.append(i-1)

        if everyone:
            print("권병장님, 중대장님이 찾으십니다")
        else:
            if 0 in rem:
                print("엄마 나 전역 늦어질 것 같아")
            else:
                rem.reverse()
                for elem in rem:
                    del dist_ppl[elem]
                    del dist_thr[elem]

                noteveryone = True
                for i in range(1, len(dist_ppl)):
                    if dist_ppl[i] - dist_ppl[i-1] > dist_thr[i-1]:
                        noteveryone = False
                        break

                if noteveryone:
                    print("권병장님, 중대장님이 찾으십니다")
                else:
                    print("엄마 나 전역 늦어질 것 같아")

        # while idx_ppl < len(dist_ppl) and idx_thr < len(dist_thr):
        #     cur_diff = dist_ppl[idx_ppl] - dist_ppl[idx_pprev]
        #     if cur_diff <= dist_thr[idx_thr]:
        #         prev_avail = True
        #         idx_ppl += 1
        #     else:
        #         if prev_avail:
        #             # available until previous person
        #             idx_pprev = idx_ppl - 1
        #             idx_thr += idx_ppl - 1
        #             prev_avail = False
        #         else:
        #             break

        # if idx_ppl == len(dist_ppl):
        #     print("권병장님, 중대장님이 찾으십니다")
        # else:
        #     print("엄마 나 전역 늦어질 것 같아")
    else:
        print("권병장님, 중대장님이 찾으십니다")
