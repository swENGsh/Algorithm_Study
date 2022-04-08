from collections import deque
def bfs():
    while q :
        n = q.popleft()
        if n == K:
            print(v[K] - 1)
            return
        for i in [n-1, n+1, n*2]:
            if 0 <= i <= 100000 and v[i] == 0:
                v[i] = v[n] + 1
                q.append(i)

N, K = map(int, input().split())
q = deque()
q.append(N)
v = [0] * 100001
v[N] = 1
bfs()
