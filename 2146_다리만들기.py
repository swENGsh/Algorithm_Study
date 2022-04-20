import sys;sys.stdin = open('2146.txt')

from collections import deque

#첫번째 bfs로 방문 정보에 각 섬의 번호를 나눠주기
def bfs1(r, c):
    global cnt
    q = deque()
    q.append((r, c))
    v[r][c] = cnt
    while q:
        r, c = q.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0<= nr < N and 0<= nc < N and arr[nr][nc] != 0 and v[nr][nc] == 0:
                v[nr][nc] = cnt
                q.append((nr, nc))

#두번째 bfs로 만든 각 섬의 번호가 담긴 v와, 새롭게 거리정보를 저장할 리스트를 생성해서 짧은 거리 구하기
def bfs2(i):
    global ans
    q = deque()
    # 거리를 저장할 리스트
    d = [[-1] * N for _ in range(N)]
    for j in range(N):
        for k in range(N):
            if v[j][k] == i:
                #섬에 해당하는 좌표를 q에 넣어주고
                q.append((j, k))
                #해당 좌표의 거리는 모두 출발지점이 될수 있으므로 0으로 설정
                d[j][k] = 0
    while q:
        r, c = q.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0<= nr < N and 0<= nc < N:
                #아직 거리를 기록하지 않았고, 바다인 부분을 만난다면 거리 기록
                if arr[nr][nc] == 0 and d[nr][nc] == -1:
                    d[nr][nc] = d[r][c] + 1
                    q.append((nr, nc))
                #다음 위치가 다른 섬이라면 거리의 최소값 구해주기
                if arr[nr][nc] != 0 and d[nr][nc] == -1:
                    if ans > d[r][c]:
                        ans = d[r][c]
                    return
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * N for _ in range(N)]
ans = 0xffffff
#각 섬의 번호, 1번 섬부터 시작
cnt = 1
for r in range(N):
    for c in range(N):
        if arr[r][c] == 1 and v[r][c] == 0:
            bfs1(r, c)
            cnt += 1
#섬의 개수 -1만큼 반복을 돌면서, bfs2를 이용해 각 섬에서 다른 섬까지의 거리 구하기
for i in range(1, cnt):
    bfs2(i)
print(ans)