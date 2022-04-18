import sys
sys.stdin = open('2636.txt')

from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def not_cheeze():
    q = deque()
    q.append((0,0))
    visit[0][0] = 1
    cheese_sum = 0
    while q:
        r,c = q.popleft()
        for d in range(4):
            nr, nc = r+dr[d], c+dc[d]
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
                if dish[nr][nc] == 0:
                    visit[nr][nc] = 1
                    q.append((nr,nc))
                else:
                    dish[nr][nc] = 0
                    visit[nr][nc] = 1
                    cheese_sum += 1
    cheese.append(cheese_sum)
    return cheese_sum

N,M = map(int,input().split())

dish = [list(map(int,input().split())) for _ in range(N)]

cheese_cnt = 0

cheese = []

melt = -1
while True:
    melt += 1
    visit = [[0]*M for _ in range(N)]
    cheese_cnt = not_cheeze()
    if cheese_cnt == 0:
        cheese_cnt = cheese[-2]
        break

print(melt)
print(cheese_cnt)
