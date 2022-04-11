# from heapq import heappop, heappush
#
# T = int(input())
# for _ in range(T):
#     N, M = map(int, input().split())
#     data = list(map(int, input().split()))
#     Q = []
#     cnt = 0
#     for i in range(N):
#         heappush(Q, (data[i], i))
#     while Q:
#         cnt += 1
#         primary, page = heappop(Q)
#         if page == M:
#             print(cnt)
#             break

from collections import deque
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    Q = list(map(int, input().split()))
    idx = [0 for _ in range(N)]
    idx[M] = 'ans'
    cnt = 0
    while Q:
        if Q[0] == max(Q):
            cnt += 1
            if idx[0] == 'ans':
                print(cnt)
                break
            else:
                Q.pop(0)
                idx.pop(0)
        else:
            Q.append(Q.pop(0))
            idx.append(idx.pop(0))

