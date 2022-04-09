dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
def spin():
    global d
    d -= 1
    if d == -1:
        d = 3

N, M = map(int, input().split())
r, c, d = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
cnt = 1
d_cnt = 0
visit[r][c] = 1
while True:
    spin()
    nr, nc = r + dr[d], c + dc[d]
    # if 0 <= nr < N and 0 <= nc < M:
    if data[nr][nc] == 0 and not visit[nr][nc]:
        visit[nr][nc] = 1
        cnt += 1
        r, c = nr, nc
        d_cnt = 0
        continue
    else:
        d_cnt += 1
    if d_cnt == 4:
        mr, mc = r - dr[d], c - dc[d]
        if not data[mr][mc]:
            r, c = mr, mc
        else:
            break
        d_cnt = 0

print(cnt)
