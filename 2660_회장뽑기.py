'''
분류 : 그래프, BFS, 플로이드 와샬
그림을 그려 봄으로써 쉽게 이해할 수 있었던 문제
'''
def BFS(V):
    visit = [0] * (N + 1)
    Q = [V]
    # 회원간 친구 관계 파악
    while Q:
        u = Q.pop(0)
        for x in G[u]:
            if x != V and visit[x] == 0:
                visit[x] = visit[u] + 1
                Q.append(x)

    # 가장 멀리 있는 친구로 점수가 결정남
    ans[V] = max(visit)

N = int(input())
G = [[] for _ in range(N+1)]
ans = [0] * (N+1) # 점수를 저장할 리스트

while True:
    x, y = map(int, input().split())
    if x == -1:
        break
    else:
        G[x].append(y)
        G[y].append(x)

for i in range(1, N+1):
    BFS(i)

ans.pop(0) # 후보 계산을 위해 의미 없는 값을 제거

# 회장 후보의 점수는 점수의 최소값이며, 후보의 수는 해당 점수를 가진 회원 수
print(min(ans), ans.count(min(ans)))
# 회장 후보 출력
for i in range(N):
    if ans[i] == min(ans):
        print(i+1, end=' ')

