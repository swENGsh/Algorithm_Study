import sys
sys.stdin = open('imput.txt')

def DFS(n):
    global ans
    visit[n] = 1
    for w in G[n]: # 인접 정점을 찾음
        if not visit[w]:
            ans += 1
            DFS(w)

N = int(input())
K = int(input())
G = [[] for _ in range(N + 1)]
visit = [0] * (N+1)
ans = 0

for _ in range(K):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

DFS(1)

print(ans)