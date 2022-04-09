dr, dc = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0 ,-1, 1, -1, 1, -1, 1]

def bfs(i, j):
    # global cnt
    q =[]
    # cnt +=1
    q.append((i, j))
    while q:
        r, c = q.pop(0)
        for k in range(8):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < h and 0 <= nc < w and not visit[nr][nc]:
                if data[nr][nc] == 1:
                    visit[nr][nc] = 1
                    # cnt += 1
                    # data[nr][nc] = 0
                    q.append((nr, nc))

while True:
    w, h = map(int, input().split())
    if w==0 and h == 0:
        break
    data = [list(map(int, input().split())) for _ in range(h)]
    visit = [[0] * w for _ in range(h)]
    cnt = 0
    for r in range(h):
        for c in range(w):
            if data[r][c] == 1 and not visit[r][c]:
                cnt += 1
                bfs(r, c)
    print(cnt)