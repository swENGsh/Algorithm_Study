import sys;sys.stdin=open('17144.txt')
R, C, T = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

#공기청정기 위아래 r좌표 찾기
U = -1
D = -1

#공기청정기 위치 찾기
for i in range(R):
        if arr[i][0] == -1:
            U = i
            D = i + 1
            break

#미세먼지 1회 확산 구하기
def spread():
    v = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if arr[r][c] > 0:
                left = 0
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] != -1:
                        #v에는 확산된 먼지 저장, arr은 확산 후 남은 미세먼지들만 저장 나중에 합쳐주기.
                        v[nr][nc] = v[nr][nc] + arr[r][c] // 5
                        left += arr[r][c] // 5
                arr[r][c] -= left

    for r in range(R):
        for c in range(C):
            arr[r][c] += v[r][c]

#공기청정기 위쪽 좌표로 회전시키기
def up_dust():
    r, c = U, 1
    before = 0
    direct = 0
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]
    #동 북 서 남 방향으로 순회
    while True:
        nr = r + dr[direct]
        nc = c + dc[direct]
        if r == U and c == 0:
            break
        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            direct += 1
            continue
        arr[r][c], before = before, arr[r][c]
        r, c = nr, nc

def down_dust():
    r, c = D, 1
    before = 0
    direct = 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    #동 북 서 남 방향으로 순회
    while True:
        nr = r + dr[direct]
        nc = c + dc[direct]
        if r == D and c == 0:
            break
        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            direct += 1
            continue
        arr[r][c], before = before, arr[r][c]
        r, c = nr, nc

for _ in range(T):
    spread()
    up_dust()
    down_dust()

ans = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] != 0 and arr[i][j] != -1:
            ans += arr[i][j]
print(ans)

