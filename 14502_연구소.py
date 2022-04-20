

def spread():
    dump_lab = [item[:] for item in lab] # 바이러스 테스트를 진행할 임시 배열

    # 벽 세우기
    for c in range(len(pick)):
        a, b = pick[c]
        dump_lab[a][b] = 1

    # 바이러스 위치를 확인하고 퍼트리기 위한  dump_virus
    dump_virus = [item[:] for item in virus]

    while dump_virus:
        r, c = dump_virus.pop(0)

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and dump_lab[nr][nc] == 0:
                dump_lab[nr][nc] = 2 # 바이러스를 퍼트리고,
                dump_virus.append([nr, nc]) # 다시 전염


    cnt = 0 # 안전 지역의 위치를 확인
    for u in range(N):
        for v in range(M):
            if dump_lab[u][v] == 0:
                cnt += 1

    return cnt

def comb(n, r, start):
    global max_cnt
    if r == 0: # 3개의 후보를 전부 다 선정하였으므로
        dump_cnt = spread()
        if max_cnt < dump_cnt:
            max_cnt = dump_cnt
        return
    else:
        for m in range(start, n): # wall의 범위 내에서
            pick.append(wall[m]) # 한가지를 선정
            comb(n, r-1, m+1) # 다음 후보를 선정하기 위해 다시 호출
            pick.pop() # 다음 후보를 삽입하기 위해 이전 후보를 제거


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

wall = [] # 벽을 세울 수 있는 위치
pick = [] # 벽을 세울 수 있는 3군데 위치를 저장
virus = [] # 바이러스의 위치를 저장
max_cnt = 0 # 안전 영역의 최댓값


# 벽을 세울 수 있는 위치 확인
for i in range(N):
    for j in range(M):
        # 빈 칸
        if lab[i][j] == 0:
            wall.append([i, j])
        # 바이러스
        if lab[i][j] == 2:
            virus.append([i, j])

x = len(wall)
# 벽을 세울 수 있는 위치 중 3군데를 선정
# 전체 후보 위치, 선정할 수, 시작 값
comb(x, 3, 0)

print(max_cnt)
