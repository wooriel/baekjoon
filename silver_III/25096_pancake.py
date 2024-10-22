# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque


if __name__ == "__main__":
    _test = int(stdin.readline())

    for i in range(1, _test+1):
        num = int(stdin.readline())
        _lst = list(map(int, stdin.readline().split()))
        count = 0
        _max = 0
        _pancake = deque()
        _pancake.extend(_lst)
        while len(_pancake) > 1:
            left = _pancake.popleft()
            right = _pancake.pop()
            if _max > max(left, right):
                continue
            else:
                # _max가 제일 큰게 아닐경우, 하나만 빼고 나머지 더 큰 애는 넣는다
                if left > right:
                    _pancake.appendleft(left)
                else:
                    _pancake.append(right)
                cur_min = min(left, right)
                if _max <= cur_min:
                    # _max가 가장 작거나 같은 경우 count 하나 올려줌
                    count += 1
                    _max = cur_min
        if len(_pancake) > 0:
            # pop last elem
            last = _pancake.pop()
            if _max <= last:
                count += 1
                # _max = last

        # 항상 양쪽을 빼야하는게 아니므로, 룹으로 2개씩 볼 수는 없음

        print("Case #{}: {}".format(i, count))
