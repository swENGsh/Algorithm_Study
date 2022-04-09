import copy


def check(x, y, n, yeon, som):
    global ans
    if n == 7:
        if som == 7 or yeon > 3:
            return
        else:
            print(see)
            ans += 1
            return

    for k in range(4):
        nx = x + dr[k]
        ny = y + dc[k]
        if 0 <= nx < 5 and 0 <= ny < 5 and visit[nx][ny] == 0:
            visit[nx][ny] = 1
            if princess[nx][ny] == 'Y':
                yeon += 1
            else:
                som += 1
            see[nx][ny] = princess[nx][ny]
            check(nx, ny, n+1, yeon, som)
            visit[nx][ny] = 0
            see[nx][ny] = 0

princess = [list(input()) for _ in range(5)]
visit = [[0] * 5 for _ in range(5)]
see = [[0] * 5 for _ in range(5)]
ans = 0 # 정답 변수

# 7공주는 가로나 세로에 인접해야함
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
# 시작 위치 선정
for i in range(5):
    for j in range(5):
        if visit[i][j] == 0:
            visit[i][j] = 1
        if princess[i][j] == 'Y':
            ye, so = 1, 0
        else:
            ye, so = 0, 1
        check(i, j, 0, ye, so)

print(ans)