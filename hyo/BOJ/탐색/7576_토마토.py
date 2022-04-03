import sys; sys.stdin = open('7576.txt')
from collections import deque
def BFS():
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < M and 0 <= ny < N and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                q.append([nx, ny])
def find_day():
    global day
    for i in range(M):
        for j in range(N):
            if box[i][j] == 0:
                return -1
            elif box[i][j] > day:
                day = box[i][j]
    return day - 1

N, M = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(M)]
q = deque()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for i in range(M):
    for j in range(N):
        if box[i][j] == 1:
            q.append([i, j])
BFS()
day = 1
print(find_day())
