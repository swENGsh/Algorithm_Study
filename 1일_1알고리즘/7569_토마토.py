from collections import deque

def BFS():
    global over
    while Q:
        z, r, c = Q.popleft()
        for k in range(6):
            nr = r + dr[k]
            nc = c + dc[k]
            nz = z + dz[k]
            if 0 <= nr < N and 0 <= nc < M and 0 <= nz < H and tomato[nz][nr][nc] == 0 and visit[nz][nr][nc] == 0:
                over -= 1
                if over == 0:
                    return visit[z][r][c]
                else:
                    Q.append([nz, nr, nc])
                    visit[nz][nr][nc] = visit[z][r][c] + 1
    if over != 0:
         return -1

M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visit = [[[0] * M for _ in range(N)] for _ in range(H)]


dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

over = 0 # 익혀야할 토마토 개수
Q = deque([])

for i in range(H):
    for j in range(N):
        for l in range(M):
            if tomato[i][j][l] == 1:
                Q.append([i, j, l])
                visit[i][j][l] = 1
            if tomato[i][j][l] == 0:
                over += 1

ans = 0
if over == 0:
    print(ans)
else:
    ans = BFS()
    print(ans)