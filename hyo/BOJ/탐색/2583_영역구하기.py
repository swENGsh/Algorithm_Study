import sys; sys.stdin = open('2583.txt')

from collections import deque

def BFS(x, y):
    arr[x][y] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] == 0:
                cnt +=1
                arr[nx][ny] = 1
                q.append([nx, ny])
    return cnt

M, N, K = map(int, input().split())
arr = [[0]*N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1
#print(arr)
q = deque()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
result = []
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            q.append([i, j])
            res = BFS(i, j)
            result.append(res)
print(len(result))
result = sorted(result)
for k in result:
    print(k, end=' ')