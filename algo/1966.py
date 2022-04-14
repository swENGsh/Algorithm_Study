from collections import deque

import sys; sys.stdin = open('1966.txt')

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    status = 0

    arr = list(map(int, input().split()))

    visit = [i for i in range(N)]

    status = visit[M]

    cnt = 0
    while arr:
        if arr[0] == max(arr):
            cnt += 1

            if visit[0] == status:
                print(cnt)
                break
            arr.pop(0)
            visit.pop(0)
        else:
            a = arr.pop(0)
            v = visit.pop(0)
            arr.append(a)
            visit.append(v)
