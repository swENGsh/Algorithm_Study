from collections import deque

dz, dr, dc = [0, 0, 0, 0, -1, 1], [0, 0, -1, 1, 0, 0], [-1, 1, 0, 0, 0, 0]

def BFS():
    while q:
        z, r, c = q.popleft()

        for k in range(6):
            nz, nr, nc = z + dz[k], r + dr[k], c + dc[k]

            if 0 <= nz < Z and 0 <= nr < N and 0 <= nc < M:
                if tomato[nz][nr][nc] == 0:
                    q.append((nz, nr, nc))
                    # BFS의 깊이가 깊어질 때 마다 체크해줘야하므로
                    tomato[nz][nr][nc] = tomato[z][r][c] + 1

M, N, Z = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(Z)]

# ZxNxM 배열에서 1인 곳들을 모두 큐에 넣어주기 위해서 미리 큐 생성
q = deque()
zero_cnt = 0
for z in range(Z):
    for r in range(N):
        for c in range(M):
            # 1인 곳들을 찾아서 큐에 모두 넣어주고 방문체크
            if tomato[z][r][c] == 1:
                q.append((z, r, c))
            if tomato[z][r][c] == 0:
                zero_cnt += 1

BFS()
ans = -1
not_tomato_cnt = False
if zero_cnt == 0:
    print(0)
else:
    for z in tomato:
        for r in z:
            for c in r:
                if c == 0:
                    not_tomato_cnt = True
                if ans < c:
                    ans = c

    if not_tomato_cnt:
        print(-1)
    else:
        print(ans - 1)