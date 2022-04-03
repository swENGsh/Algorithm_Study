import sys; sys.stdin = open('7569.txt')
from collections import deque
def BFS():
    while q:
        z, x, y = q.popleft()
        for k in range(6):
            nz, nx, ny = z + dh[k], x + dx[k], y + dy[k]
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and box[nz][nx][ny] == 0:
                box[nz][nx][ny] = box[z][x][y] + 1
                q.append([nz, nx, ny])
def find_day():
    global day
    for h in range(H):
        for i in range(M):
            for j in range(N):
                if box[h][i][j] == 0:
                    return -1
                elif box[h][i][j] > day:
                    day = box[h][i][j]
    return day - 1

N, M, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(M)] for _ in range(H)]
q = deque()
dx, dy, dh = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]
for h in range(H):
    for r in range(M):
        for c in range(N):
            if box[h][r][c] == 1:
                q.append([h, r, c])
BFS()
day = 1
print(find_day())
