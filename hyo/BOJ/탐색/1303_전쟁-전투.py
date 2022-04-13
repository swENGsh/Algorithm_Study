import sys; sys.stdin = open('1303.txt')
from collections import deque

def BFS():
    global tmp
    cnt = 1
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < M:
                if tmp == 'W' and army[nr][nc] == 'W':
                    army[nr][nc] = 'C'
                    q.append((nr, nc))
                    cnt += 1
                elif tmp == 'B' and army[nr][nc] == 'B':
                    army[nr][nc] = 'C'
                    q.append((nr, nc))
                    cnt += 1
    return cnt ** 2


M, N = map(int, input().split())
army = [list(input().strip()) for _ in range(N)]
q = deque()
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

power_W = power_B = 0
for i in range(N):
    tmp = ''
    for j in range(M):
        if army[i][j] == 'W':
            tmp = 'W'
            army[i][j] = 'C'
            q.append((i, j))
            result = BFS()
            power_W += result
        elif army[i][j] == 'B':
            tmp = 'B'
            army[i][j] = 'C'
            q.append((i, j))
            result = BFS()
            power_B += result

print(power_W, power_B)