from collections import deque

def BFS():
    global over
    while Q:
        r, c = Q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and tomato[nr][nc] == 0 and visit[nr][nc] == 0:
                over -= 1
                if over == 0:
                    return visit[r][c]
                else:
                    Q.append([nr, nc])
                    visit[nr][nc] = visit[r][c] + 1
    if over != 0:
         return -1

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

over = 0 # 익혀야할 토마토 개수
sr = sc = 0 # 토마토가 담긴 위치
Q = deque([])

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            Q.append([i, j])
            visit[i][j] = 1
        if tomato[i][j] == 0:
            over += 1

ans = 0
if over == 0:
    print(ans)
else:
    ans = BFS()
    print(ans)