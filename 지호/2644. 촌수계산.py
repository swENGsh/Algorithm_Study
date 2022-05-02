from collections import deque

def bfs(num):
    visit = [-1] * (n + 1)
    visit[num] = 0
    Q = deque()
    Q.append(num)
    while Q:
        v = Q.popleft()
        for w in arr[v]:
            if visit[w] == -1:
                if w == i:
                    visit[w] = visit[v] + 1
                    return visit[w]
                else:
                    visit[w] = visit[v] + 1
                    Q.append(w)

    return visit[i]


n = int(input())
i, j = map(int, input().split())
m = int(input())
arr = [[]for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

print(bfs(j))

# print(arr)