import sys;sys.stdin = open('14502.txt')
from collections import deque

def bfs():
    global max_cnt
    visited = [[-1] * M for _ in range(N)]
    q = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                q.append((i, j))
                visited[i][j] = 2
    while q:
        r, c = q.popleft()
        for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr <N and 0 <= nc < M and visited[nr][nc] == -1 and arr[nr][nc] == 0:
                visited[nr][nc] = 0
                q.append((nr, nc))
    cnt = 0
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 0 and visited[r][c] == -1:
                cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt

def wall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(cnt + 1)
                arr[i][j] = 0

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    wall(0)
    print(max_cnt)




