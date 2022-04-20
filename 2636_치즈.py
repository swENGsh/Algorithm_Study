from collections import deque

# 녹은 치즈의 개수를 확인할 배열
def BFS():
    global cnt # 남아있는 치즈의 개수
    melt = []  # 녹여야할 치즈를 저장할 리스트
    visit = [[0] * M for _ in range(N)]  # 방문 여부를 확인할 배열
    Q.append([0, 0])
    visit[0][0] = 1
    
    while Q:
        r, c = Q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            # 방문안한 영역 중
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
                visit[nr][nc] = 1
                if cheese[nr][nc] == 0: # 공기라면 다시 탐색을 진행해야 함
                    Q.append([nr, nc])
                elif cheese[nr][nc] == 1: # 치즈라면 녹여주어야함
                    melt.append([nr, nc])
                    cnt -= 1
    
    # 치즈를 녹여줌
    for c in range(len(melt)):
        a, b = melt[c]
        cheese[a][b] = 0

    # 마지막 작업인지 확인
    if cnt == 0: # 마지막 작업일 경우, 치즈가 전부 녹게되었으므로
        return len(melt)
    else: # 마지막 작업이 아닐 경우, 다시 시작해야함
        return 0

N, M = map(int, input().split()) # N : 행, M : 열
cheese = [list(map(int, input().split())) for _ in range(N)]


ans1 = 0 # 녹는시간

# 네방향에 모두 치즈가 있는 경우는 녹지 않으므로 델타로 확인
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

cnt = 0 # 남아있는 치즈 개수의 확인
for i in range(N):
    for j in range(M):
        if cheese[i][j] == 1:
            cnt += 1

Q = deque() # 녹인 치즈의 영역을 확인할 큐
# 공기와 맞다은 영역을 확인해 치즈일 경우, 녹여줌
# 단, 실시간으로 녹이면 공기의 영역이 변하므로 한번에 녹음을 표현해줌

while True:
    ans1 += 1
    res = BFS()
    if res != 0: # 마지막 작업이므로
        print(ans1)
        print(res)
        break
