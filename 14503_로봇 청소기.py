import sys;sys.stdin = open('14503.txt')
N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for i in range(N)]
#처음 위치 청소 처리, 회전한 횟수 세기
visited[r][c] = 1
cnt = 1
turn_cnt = 0
#북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def turn():
    global d
    d -= 1
    if d == -1:
        d = 3
while True:
    turn()
    nr, nc = r + dr[d], c + dc[d]
    if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0 and visited[nr][nc] == 0:
        visited[nr][nc] = 1
        cnt += 1
        r, c = nr, nc
        turn_cnt = 0
        continue
    else:
        turn_cnt += 1

    if turn_cnt == 4:
        nr, nc = r - dr[d], c - dc[d]
        if room[nr][nc] == 0:
            r, c = nr, nc
        else:
            break
        turn_cnt = 0
print(cnt)

