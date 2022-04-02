import sys
sys.stdin = open('2667.txt')
from collections import deque

from collections import deque

def BFS(r, c, cnt):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    q = deque()
    q.append((r, c))
    visited[r][c] = cnt
    while q:
        r, c = q.popleft()

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc <N:
                if map[nr][nc] == 1 and visited[nr][nc] == 0:
                    q.append((nr, nc))
                    visited[nr][nc] = cnt


N = int(input())
map = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
# print(map)
# print(visited)
cnt = 0
for r in range(N):
    for c in range(N):
        if map[r][c] == 1 and not visited[r][c]:
            cnt += 1
            BFS(r, c, cnt)
            # print(cnt)

ans_lst=[]
# print(visited)
for i in range(1, cnt+1):
    ans = 0

    for r in range(N):
        for c in range(N):
            if visited[r][c] == i:
                ans +=1
    ans_lst.append(ans)

print(cnt)
new_ans = sorted(ans_lst)
for i in range(len(new_ans)):
    print(new_ans[i])