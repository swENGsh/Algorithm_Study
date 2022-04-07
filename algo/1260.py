import sys
sys.stdin = open('1260.txt')

from collections import deque

def dfs(n,lst):
    for i in A[n]:
        if dfs_visit[i] == 0:
            dfs_visit[i] = 1
            lst.append(i)
            dfs(i,lst)

    return
def bfs(n,lst):
    q = deque()
    q.append(n)
    bfs_visit[n] = 1
    while q:
        v = q.popleft()
        lst.append(v)
        for i in A[v]:
            if bfs_visit[i] == 0:
                q.append(i)
                bfs_visit[i] = 1
    print(*lst)
    return


N,M,V = map(int, input().split())

A = [[] for _ in range(N+1)]
dfs_visit = [0] * (N+1)
bfs_visit = [0] * (N+1)
for _ in range(M):
    s,e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(1,N+1):
    A[i].sort()

arr = [V]
dfs_visit[V] = 1

dfs(V,arr)
print(*arr)
arr = []
bfs(V,arr)

