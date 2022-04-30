import sys;sys.stdin=open('2260.txt')
from collections import deque

def bfs(r, c, d):
    q = deque()
    q.append((r, c, d))
    v[r][c][d] = 1
    while q:
        r, c, d = q.popleft()
        if (r, c) == (N - 1, M - 1):
            return v[r][c][d]
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 1 and d == 0:
                    v[nr][nc][1] = v[r][c][0] + 1
                    q.append((nr, nc, 1))
                elif arr[nr][nc] == 0 and v[nr][nc][d] == 0:
                    v[nr][nc][d] = v[r][c][d] + 1
                    q.append((nr, nc, d))
    return -1
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
v = [[[0]*2 for _ in range(M)] for _ in range(N)]

print(bfs(0, 0, 0))

# 시간초과 코드
# def bfs():
#     global max_cnt
#     v = [[-1] * M for _ in range(N)]
#     v[0][0] = 1
#     q = deque()
#     q.append((0, 0))
#     while q:
#         r, c = q.popleft()
#         for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             nr, nc = r + dr, c + dc
#             if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == '0' and v[nr][nc] == -1:
#                 v[nr][nc] = v[r][c] + 1
#                 q.append((nr, nc))
#     cnt = v[N-1][M-1]
#     if max_cnt < cnt:
#         max_cnt = cnt
#
# N, M = map(int, input().split())
# arr = [list(input()) for _ in range(N)]
#
# max_cnt = -1
# for r in range(N):
#     for c in range(M):
#         if arr[r][c] == '1':
#             arr[r][c] =  '0'
#             bfs()
#             arr[r][c] = '1'
#
# print(max_cnt)
