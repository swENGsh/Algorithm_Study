import sys;sys.stdin = open('1260.txt')
from collections import deque

def dfs(n):
    #출발점 출력 및 방문표시
    print(n, end=' ')
    visited[n] = 1
    #n과 연결된 간선 중에서 아직 방문안한 곳이 있다면 다시 탐색
    for i in G[n]:
        if visited[i] == 0:
            dfs(i)

def bfs(n):
    q = deque()
    visited[n] = 1
    q.append(n)
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in G[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1

for tc in range(int(input())):
    #N은 정점의 수, M은 간선의 수, V는 출발할 정점의 번호
    N, M, V = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)
    for i in range(M):
        s, e = map(int, input().split())
        G[s].append(e)
        G[e].append(s)

    #정렬된 순서로 탐색하기 위해 간선 정보 정렬하기
    for i in range(N + 1):
        G[i].sort()

    dfs(V)
    print()
    visited = [0] * (N + 1)
    bfs(V)
    print()
