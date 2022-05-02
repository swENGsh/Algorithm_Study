import sys
sys.stdin = open('2206.txt')

from collections import deque

N, M = map(int, input().split())

visit = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visit[0][0][0] = 1

arr = [list(map(int, input())) for _ in range(N)]


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(start, end, b):
    q = deque()
    q.append((start, end, b))

    while q:
        r, c, cnt = q.popleft()
        if r == N - 1 and c == M - 1:
            return visit[r][c][cnt]
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if arr[nr][nc] == 1 and cnt == 0 :
                visit[nr][nc][1] = visit[r][c][0] + 1
                q.append((nr, nc, 1))
            elif arr[nr][nc] == 0 and visit[nr][nc][cnt] == 0:
                visit[nr][nc][cnt] = visit[r][c][cnt] + 1
                q.append((nr, nc, cnt))
    return -1


print(bfs(0, 0, 0))
