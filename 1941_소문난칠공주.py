# 1차원 배열에서의 7공주 위치(0 ~ 24), 선택한 공주 수, 이다솜파의 수(4이상, 7미만이어야함)
def choice(cnt, sel, S_cnt):
    global ans
    # 남은 sel을 모두 선택해도 이다솜파가 우위를 잡지 못하는 경우
    if S_cnt + (7 - sel) < 4: return
    # 7공주 선택 완료
    if sel == 7:
        # 이다솜 파의 조건에 맞을 경우, 인접 확인
        if S_cnt >= 4 and bfs():
            ans +=1
        return
    # 배열을 모두 확인한 경우
    if cnt == 25: return

    # 7공주 선택하기
    # 행과 열 파악
    r = cnt // 5
    c = cnt % 5
    # sel번째로 선택한 7공주 위치 삽입
    select[sel] = (r, c)
    # 이번 셀에서 7공주를 선택한 경우
    choice(cnt + 1, sel + 1, S_cnt + 1 if princess[r][c] == 'S' else S_cnt)
    # 이번 셀에서 7공주를 선택하지 않은 경우
    choice(cnt+1, sel, S_cnt)
    return

# 인접 확인
def bfs():
    visited = [[0]*5 for _ in range(5)]
    check = 1

    # 첫번째 7공주의 위치 표시
    for i in range(1, 7):
        visited[select[i][0]][select[i][1]] = 1

    Q = []
    # 첫번째 7공주의 위치를 Q에 삽입
    Q.append((select[0][0], select[0][1]))
    
    while Q:
        r, c = Q.pop(0)
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            # 범위 확인
            if nr < 0 or nc < 0 or nr >= 5 or nc >= 5:
                continue
            # 인접한 곳에 다른 공주가 있는 경우
            if visited[nr][nc]:
                # 인원 수를 한명 추가 
                check += 1
                # 7공주를 확인했으니 방문 표시 지우기
                visited[nr][nc] = 0
                # Q에 삽입
                Q.append((nr, nc))
                # 7명 다 확인한 경우 True
                if check == 7:
                    return True
    return False

# 공주 배열
princess = [input() for _ in range(5)]
# 7공주 선택 여부 확인 배열
select = [-1] * 7
ans = 0 # 정답 변수

# 7공주는 가로나 세로에 인접해야함
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 7공주의 위치 선택
# 1차원 배열에서의 7공주 위치(0 ~ 24), 선택한 공주 수, 이다솜파의 수(4이상, 7미만이어야함)
choice(0, 0, 0)
print(ans)
