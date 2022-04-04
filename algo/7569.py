import sys
sys.stdin = open('7569.txt')
from collections import deque

dr = [-1, 1, 0, 0, 0, 0] #상하좌우
dc = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

#안익은 토마토가 있는 경우를 체크
def tomato_check(lst):
    for h in range(H):
        for n in range(M):
            for m in range(N):
                if lst[h][n][m] == 0:
                    return -1


def tomato_box():
    if len(q) == 0:
        return 0
    while q:
        z, r, c, check = q.popleft()
        for d in range(6):
            nz, nr, nc = z+dz[d], r+dr[d], c+dc[d]
            if 0 <= nz < H and 0 <= nr < M and 0 <= nc < N  and arr[nz][nr][nc] == 0 :
                arr[nz][nr][nc] = 1
                q.append((nz, nr,nc,check+1))
    return check

N, M, H = map(int, input().split())

arr = [[list(map(int, input().split())) for _ in range(M)] for _ in range(H)]

q = deque()

for h in range(H):
    for i in range(M):
        for j in range(N):
            if arr[h][i][j] == 1:
                q.append((h,i,j,0))

tmt = tomato_box()
not_tmt = tomato_check(arr)

if not_tmt:
    print(not_tmt)
else:
    print(tmt)