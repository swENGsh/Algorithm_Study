'''
1. 반복문을 통해 벽을 3개 생성 (wall 함수)
2. BFS를 통해서 값이 0인 부분들 탐색
3. visited를 쓰는 이유 - virus_map 원본 자체가 손상되는것을 막기 위해서
4. python으로 제출 시 시간초과 => 이 부분에 대해서는 연구가 필요할듯?
5. deep copy를 통한 풀이도 존재한다.

'''

from collections import deque
# import sys
# dr, dc = [0, 0, -1, 1], [-1, 1, 0, 0]
#
# def BFS():
#     global max_cnt
#     visited = [[-1] * M for _ in range(N)]
#     q = deque()
#     for r in range(N):
#         for c in range(M):
#             if virus_map[r][c] == 2:
#                 q.append((r, c))
#                 # visited 에도 virus가 있는 위치를 기록해준다. 나중에 방문하지 않은 곳들을 체크하기 위해서
#                 visited[r][c] = 2
#
#     while q:
#         r, c = q.popleft()
#         for k in range(4):
#             nr, nc = r + dr[k], c + dc[k]
#
#             if 0 <= nr < N and 0 <= nc < M:
#                 # 빈 칸이고 방문하지 않았다면
#                 if virus_map[nr][nc] == 0 and visited[nr][nc] == -1:
#                     # 방문체크
#                     visited[nr][nc] = 0
#                     q.append((nr, nc))
#
#     safe_cnt = 0
#     for i in range(N):
#         for j in range(M):
#             # virus 맵에서 빈 칸이고 방문하지 않은 곳이라면 바이러스가 침투하지 않은 곳.
#             if virus_map[i][j] == 0 and visited[i][j] == -1:
#                 safe_cnt += 1
#
#     if max_cnt < safe_cnt:
#         max_cnt = safe_cnt
#
#
# def wall(cnt):
#     if cnt == 3:
#         BFS()
#         return
#
#     for i in range(N):
#         for j in range(M):
#             if virus_map[i][j] == 0:
#                 virus_map[i][j] = 1
#                 wall(cnt + 1)
#                 virus_map[i][j] = 0
#
#
# N, M = map(int, input().split())
#
# virus_map = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
# max_cnt = 0
# wall(0)
#
# print(max_cnt)


#==================================

# 슬라이싱으로 배열 복사하기

from collections import deque
'''
pypy3 
1. visited를 사용하지 않고 슬라이싱을 통해 virus_map을 카피 
2. wall 함수를 for 문을 쓰지 않고 백트래킹 형식으로 작성. ==> 이 부분이 가장 실행시간차이를 유의미하게 냄.
'''
import sys
dr, dc = [0, 0, -1, 1], [-1, 1, 0, 0]

def BFS():
    global max_cnt
    copy_map = [i[:] for i in virus_map]
    q = deque()
    for r in range(N):
        for c in range(M):
            if copy_map[r][c] == 2:
                q.append((r, c))

    while q:
        r, c = q.popleft()

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]

            if 0 <= nr < N and 0 <= nc < M and copy_map[nr][nc] == 0:
                    copy_map[nr][nc] = 2
                    q.append((nr, nc))

    safe_cnt = 0
    for i in range(N):
        for j in range(M):
            # virus 맵에서 빈 칸이고 방문하지 않은 곳이라면 바이러스가 침투하지 않은 곳.
            if copy_map[i][j] == 0:
                safe_cnt += 1

    max_cnt = max(max_cnt, safe_cnt)


def wall(i, j, cnt):
    if cnt > 3:
        return

    if cnt == 3:
        BFS()
        return

    if j == M:
        j = 0
        i += 1

    if i == N:
        return

    if virus_map[i][j] == 0:
        virus_map[i][j] = 1
        wall(i, j+1, cnt + 1)
        virus_map[i][j] = 0

    wall(i, j+1, cnt)

N, M = map(int, input().split())

virus_map = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
max_cnt = 0
wall(0, 0, 0)

print(max_cnt)

#==================================================
'''
pypy3
메모리 131792KB
실행시간 388ms
BFS함수 안에서 virus를 찾던걸 함수 밖으로 빼내 준 뒤
리스트에 바이러스 위치를 넣은 뒤 그걸 활용
'''
from collections import deque
import sys
dr, dc = [0, 0, -1, 1], [-1, 1, 0, 0]

def BFS():
    global max_cnt
    copy_map = [i[:] for i in virus_map]
    q = deque()
    for i in virus_list:
        q.append(i)

    while q:
        r, c = q.popleft()

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]

            if 0 <= nr < N and 0 <= nc < M and copy_map[nr][nc] == 0:
                    copy_map[nr][nc] = 2
                    q.append((nr, nc))

    safe_cnt = 0
    for i in range(N):
        for j in range(M):
            # virus 맵에서 빈 칸이고 방문하지 않은 곳이라면 바이러스가 침투하지 않은 곳.
            if copy_map[i][j] == 0:
                safe_cnt += 1

    max_cnt = max(max_cnt, safe_cnt)


def wall(i, j, cnt):
    if cnt > 3:
        return

    if cnt == 3:
        BFS()
        return

    if j == M:
        j = 0
        i += 1

    if i == N:
        return

    if virus_map[i][j] == 0:
        virus_map[i][j] = 1
        wall(i, j+1, cnt + 1)
        virus_map[i][j] = 0

    wall(i, j+1, cnt)

N, M = map(int, input().split())

virus_map = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
virus_list=[]
for r in range(N):
    for c in range(M):
        if virus_map[r][c] == 2:
            virus_list.append((r, c))


max_cnt = 0
wall(0, 0, 0)

print(max_cnt)