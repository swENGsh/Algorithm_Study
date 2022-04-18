from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c, water_height):
    Q = deque()
    Q.append((r, c))
    visit[r][c] = 1

    while Q:
        r, c = Q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                if land[nr][nc] >= water_height and visit[nr][nc] == 0:
                    visit[nr][nc] = 1
                    Q.append((nr, nc))

N = int(input())
land = [list(map(int, input().split()))for _ in range(N)]
max_limit = max(map(max, land))
min_limit = min(map(min, land))
# print(limit)
ans = 0
for water_height in range(max_limit+1):
    visit=[[0] * N for _ in range(N)]
    cnt = 0
    for r in range(N):
        for c in range(N):
            if land[r][c] >= water_height and not visit[r][c]:
                bfs(r, c, water_height)
                cnt += 1
    if ans < cnt:
        ans = cnt

print(ans)