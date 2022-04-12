import sys
sys.stdin = open('2589.txt')

from collections import deque

def BFS(start, end, cnt):
    global mx_cnt
    q = deque()
    q.append((start,end,cnt))
    visit[start][end] = 1
    while q:
        r, c, cnt = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c+dc[d]
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0 and island[nr][nc] == 'L':
                visit[nr][nc] = 1
                q.append((nr,nc,cnt+1))
                nr += dr[d]
                nc += dc[d]
        if mx_cnt < cnt:
            mx_cnt = cnt
    return

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N,M = map(int, input().split())

island = [list(input()) for _ in range(N)]

mx_cnt = 0
for i in range(N):
    for j in range(M):
        if island[i][j] == 'L':
            visit = [[0] * M for _ in range(N)]
            BFS(i,j,1)


print(mx_cnt-1)