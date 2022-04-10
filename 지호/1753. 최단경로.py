from heapq import heappop, heappush

def DIJKSTRA_PRIORITYQ(s):

    D = [0xffffff] * (V + 1)
    P = [i for i in range(V + 1)]
    visit = [False] * (V + 1)
    D[start] = 0
    Q = [[0, start]]

    while Q:
        d, u = heappop(Q)
        if visit[u]: continue

        visit[u] = True
        for v, w in G[u]:
            if not visit[v] and D[v] > D[u] + w:
                D[v] = D[u] + w
                P[v] = u
                heappush(Q, [D[v], v])
    for i in range(1, len(D)):
        if D[i] == 0xffffff:
            print("INF")
        else:
            print(D[i])
    #     print(i)
    # print(D[1:])
    # print(P[1:])


V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
start = int(input())
# INF = 0xffffff
for i in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))

DIJKSTRA_PRIORITYQ(1)