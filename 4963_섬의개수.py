import sys;sys.stdin = open('4963.txt')
from collections import deque

def bfs(r, c):
    q = deque()
    v[r][c] = 1
    q.append((r, c))
    while q:
        cr, cc = q.popleft()
        for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1], [1, 1], [1, -1], [-1, -1], [-1, 1]]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < h and 0 <= nc < w and maps[nr][nc] == 1 and v[nr][nc] == 0:
                v[nr][nc] = 1
                q.append((nr, nc))

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    maps = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    v = [[0] * w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if maps[r][c] == 1 and v[r][c] == 0:
                cnt += 1
                bfs(r, c)
    print(cnt)