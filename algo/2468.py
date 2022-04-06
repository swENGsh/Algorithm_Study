import sys
sys.stdin = open('2468.txt')
from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def safe_zone(s,e):
    q = deque()
    q.append((s,e))
    visit[s][e] = 1
    while q:
        r,c = q.popleft()
        for d in range(4):
            nr, nc = r+dr[d], c+dc[d]
            while 0 <= nr < N and 0 <= nc < N and visit[nr][nc] == 0 and arr[nr][nc] > status:
                q.append((nr,nc))
                visit[nr][nc] = 1
                nr += dr[d]
                nc += dc[d]
    return



N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

mx_cnt = -999
mn_num = 9999
mx_num = -9999

for i in range(N):
    for j in range(N):
        if arr[i][j] < mn_num:
            mn_num = arr[i][j]
        if arr[i][j] > mx_num:
            mx_num = arr[i][j]

for o in range(mn_num, mx_num+1):
    status = 0
    cnt = 0
    nn = 0
    visit = [[0] * N for _ in range(N)]
    for t in range(N):
        for h in range(N):
            if arr[t][h] > o and visit[t][h] == 0:
                status = o
                cnt += 1
                safe_zone(t,h)
    if cnt == 0:
        cnt = 1
    if mx_cnt < cnt:
        mx_cnt = cnt
print(mx_cnt)

