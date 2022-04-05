import sys
sys.stdin = open('2583.txt')

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def binary_check(s,e):
    bin_sum = 0
    q = deque()
    q.append((s,e))
    paper[s][e] = 1
    bin_sum += 1

    while q:
        r,c = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d] , c + dc[d]
            while 0 <= nr < N and 0 <= nc < M and paper[nr][nc] == 0:
                q.append((nr,nc))
                paper[nr][nc] = 1
                bin_sum += 1
                nr += dr[d]
                nc += dc[d]
    pp_binary.append(bin_sum)
    return



N, M, K = map(int, input().split())

paper = [[0]*M for _ in range(N)]

for _ in range(K):
    X1,Y1, X2, Y2 = map(int, input().split())

    for i in range(Y1, Y2):
        for j in range(X1, X2):
            if paper[i][j] == 1:
                continue
            paper[i][j] = 1

total_bin = 0
pp_binary = []
for n in range(N):
    for m in range(M-1,-1,-1):
        if paper[n][m] == 0:
            total_bin += 1
            binary_check(n,m)

pp_binary.sort()

print(total_bin)
print(*pp_binary)


