import sys;sys.stdin = open('7562.txt')
from collections import deque

def bfs():
    q = deque()
    q.append((cr, cc))
    while q:
        r, c = q.popleft()
        for dr, dc in [(-1, -2), (-2, -1), (1, 2), (2, 1), (1, -2), (2, -1), (-2, 1), (-1, 2)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and v[nr][nc] == 0:
                v[nr][nc] = v[r][c] + 1
                q.append((nr, nc))

for tc in range(int(input())):
    N = int(input())
    cr, cc = map(int, input().split())
    sr, sc = map(int, input().split())
    v = [[0] * N for _ in range(N)]
    v[cr][cc] = 1
    bfs()
    print(v[sr][sc] - 1)