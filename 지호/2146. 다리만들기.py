from collections import deque
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
N = int(input())

def bfs(r, c, cnt):
    Q = deque()
    Q.append((r, c))
    visit[r][c] = cnt
    while Q:
        r, c = Q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if ground[nr][nc] and not visit[nr][nc]:
                    visit[nr][nc] = cnt
                    Q.append((nr, nc))


def bfs2(i):
    global min_ans
    visit2 = [[0] * N for _ in range(N)]
    Q = deque()
    for r in range(N):
        for c in range(N):
            if visit[r][c] == i:
                Q.append((r, c))
                visit2[r][c] = 1
    while Q:
        r, c = Q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if visit[nr][nc] != i and visit[nr][nc]:
                    min_ans = min(min_ans, visit2[r][c])
                    return
                if visit[nr][nc] == 0 and visit2[nr][nc] == 0:
                    visit2[nr][nc] = visit2[r][c] + 1
                    Q.append((nr, nc))

ground = [list(map(int, input().split())) for _ in range(N)]
visit = [[0]*N for _ in range(N)]
cnt = 1
min_ans = 0xffffff

for r in range(N):
    for c in range(N):
        if ground[r][c] == 1 and not visit[r][c]:
            bfs(r, c, cnt)
            cnt += 1
for i in range(1, cnt):
    bfs2(i)
# print(visit)
print(min_ans-1)