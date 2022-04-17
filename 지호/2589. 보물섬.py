from collections import deque
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(r, c):
    visit = [[0] * W for _ in range(H)]
    visit[r][c] = 1
    while Q:
        r, c = Q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < H and 0 <= nc < W and not visit[nr][nc]:
                if island[nr][nc] == 'L':
                    visit[nr][nc] = visit[r][c] + 1
                    Q.append((nr, nc))
    result = 0
    for i in range(H):
        for j in range(W):
            if visit[i][j] > result:
                result = visit[r][c]
    return result

H, W = map(int, input().split())

island = [list(map(str, input())) for _ in range(H)]
ans = []
for r in range(H):
    for c in range(W):
        if island[r][c] == 'L':
            Q = deque()
            Q.append((r, c))
            ans.append(bfs(r, c))

print(max(ans)-1)