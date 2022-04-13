import sys; sys.stdin = open('1926.txt')
from collections import deque

def BFS():
    global maxv

    area = 1
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < n and 0 <= nc < m and pic[nr][nc] == 1:
                pic[nr][nc] = 0
                q.append((nr, nc))
                area += 1
    maxv = max(maxv, area)


n, m = map(int, input().split())
pic = [list(map(int, input().split())) for _ in range(n)]
q = deque()
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

cnt = maxv = 0
for i in range(n):
    for j in range(m):
        if pic[i][j] == 1:
            q.append((i, j))
            pic[i][j] = 0
            BFS()
            cnt += 1

print(cnt)
print(maxv)