from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def BFS(x, y):
    global size
    q = deque()
    arr[x][y] = 1
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] == 0:
                arr[nx][ny] = 1
                size += 1
                q.append((nx, ny))

M, N, K = map(int, input().split())
arr = [[0] * N for _ in range(M)]
for _ in range(K):
    sc, sr, ec, er = map(int, input().split())
    for i in range(sr, er):
        for j in range(sc, ec):
            arr[i][j] = 1


blank = deque()
size_list = []
cnt = 0
for r in range(M):
    for c in range(N):
        if arr[r][c] == 0:
            cnt += 1
            size = 1
            BFS(r, c)
            size_list.append(size)
print(cnt)
size_list.sort()
for i in size_list:
    print(i, end=' ')
