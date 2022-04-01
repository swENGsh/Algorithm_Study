com = int(input())
direct = int(input())

# DFS
def dfs(graph, visited, current):
    visited[current] = 1
    for i in graph[current]:
        if visited[i] != 1:
            dfs(graph, visited, i)

connect = [[] for _ in range(com + 1)]
visited = [0] * (com + 1)
for _ in range(direct):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)

dfs(connect, visited, 1)
cnt = 0
for i in visited[2:]:
    if i == 1:
        cnt += 1
print(cnt)