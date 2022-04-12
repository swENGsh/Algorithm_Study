import sys; sys.stdin = open('2468.txt')
from collections import deque
def depth_check(n):
    global maxv
    global visit
    visit = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if rain[i][j] <= n:
                visit[i][j] = 1
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                visit[i][j] = 1
                q.append([i, j])
                BFS()
                cnt += 1
    if maxv < cnt :
        maxv = cnt
    if cnt == 0:
        if n == 1:
            maxv = 1
            return
        return
    depth_check(n+1)

def BFS():
    global visit
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                q.append([nx, ny])

N = int(input())
rain = [list(map(int, input().split())) for _ in range(N)]

q = deque()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
maxv = 0
depth_check(1)
print(maxv)