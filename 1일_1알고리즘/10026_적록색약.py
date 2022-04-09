import sys
sys.stdin = open('imput.txt')

def BFS(a, b):
    Q = []
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    Q.append((a, b))
    visit[a][b] = 1

    while Q:
        r, c = Q.pop(0)
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and visit[nr][nc] == 0:
                if color[r][c] == color[nr][nc]:
                    visit[nr][nc] = 1
                    Q.append((nr, nc))
    return


N = int(input())
color = [list(input()) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
ans1 = 0
ans2 = 0
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            BFS(i, j)
            ans1 += 1

        if color[i][j] == 'G':
            color[i][j] = 'R'

visit = [[0] * N for _ in range(N)]
for m in range(N):
    for n in range(N):
        if visit[m][n] == 0:
            BFS(m, n)
            ans2 += 1

print(ans1, ans2)



