'''
분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색
백트래킹으로 시도했지만, 재귀 오류가 발생하여 bfs로 해결
'''
def check(r, c):
    global ans
    Q = [(r, c)]
    visited[r][c] = 1

    while Q:
        m, n = Q.pop(0)
        if m == x and n == y:
            print(visited[x][y]-1)
            return
        for k in range(8):
            nr = m + dr[k]
            nc = n + dc[k]

            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                Q.append((nr, nc))
                visited[nr][nc] = visited[m][n] + 1


tc = int(input())

for i in range(tc):
    N = int(input())
    a, b = map(int, input().split())
    x, y = map(int, input().split())

    # 방문 확인
    visited = [[0] * N for _ in range(N)]

    # 이동 가능 구역
    dr = [-1, -2, -2, -1, 1, 2, 2, 1]
    dc = [-2, -1, 1, 2, 2, 1, -1, -2]

    
    # 시작 좌표
    check(a, b)

