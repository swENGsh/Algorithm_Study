import sys;sys.stdin = open('2468.txt')
from collections import deque

def bfs(r, c, k):
    q = deque()
    q.append((r, c))
    v[r][c] = 1
    while q:
        r, c = q.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] > k and v[nr][nc] == 0:
                v[nr][nc] = 1
                q.append((nr, nc))

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

arr_max = max(map(max, arr))
arr_min = min(map(min, arr))


ans = 0
for k in range(0, 101):
    cnt = 0
    v = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if arr[r][c] > k and v[r][c] == 0:
                bfs(r, c, k)
                cnt += 1
                if ans <= cnt:
                    ans = cnt
print(ans)