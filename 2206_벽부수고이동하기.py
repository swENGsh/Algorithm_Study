import sys
sys.stdin = open('sample.txt')

def check(a, b, wall, now_ans):
    global ans
    # 종료 조건
    if a == (N-1) and b == (M-1):
        if now_ans < ans or ans == -1:
            ans = now_ans
        return
    # 진행 조건
    else:
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        for i in range(4):
            nr = a + dr[i]
            nc = b + dc[i]
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
                # 벽은 단 1번 무시하고 이동할 수 있음
                if matrix[nr][nc] == 1 and wall == 0: # 벽을 부순적이 없다면, 부술 수 있음
                    visit[nr][nc] = 1
                    check(nr, nc, wall + 1, now_ans + 1)
                    visit[nr][nc] = 0
                elif matrix[nr][nc] == 0:
                    visit[nr][nc] = 1
                    check(nr, nc, wall, now_ans + 1)
                    visit[nr][nc] = 0

    return

N, M = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(N)]
ans = -1
visit = [[0] * M for _ in range(N)]
visit[0][0] = 1

# 거리를 계산할 함수
# 좌표(x, y), 벽을 부순 횟수, 이동 거리
check(0, 0, 0, 1)

print(ans)