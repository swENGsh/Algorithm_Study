import sys;sys.stdin = open('7576.txt')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(graph):
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < n and 0 <= b < m and graph[a][b] == 0:
                queue.append((a, b))
                graph[a][b] = graph[x][y] + 1

def check():
    global answ
    for r in range(n):
        for c in range(m):
            if arr[r][c] == 0:
                answ = -1
                return answ
            else:
                if answ < arr[r][c]:
                    answ = arr[r][c] - 1

for tc in range(int(input())):
    m, n = map(int, input().split())
    arr = []
    queue = deque()
    for i in range(n):
        arr.append(list(map(int, input().split())))
        for j in range(m):  # 익은 토마토 큐에 저장
            if arr[i][j] == 1:
                queue.append((i, j))
    bfs(arr)
    answ = 0
    check()
    print(answ)