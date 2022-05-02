from collections import deque
#
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
#
# def first_melt_cheeze():
#     # visit[r][c] = 1
#     while Q:
#         r, c = Q.popleft()
#         for k in range(4):
#             nr, nc = r + dr[k], c + dc[k]
#
#             if 0 <= nr < H and 0 <= nc < W:
#                 if cheeze[nr][nc] == 0 and not visit[nr][nc]:
#                     visit[r][c] = 1
#                     Q.append((nr, nc))
#                 if cheeze[nr][nc] == 1:
#                     cheeze[nr][nc] = 'c'
#
# def melt_cheeze():
#     global cnt
#     while Q:
#         r, c = Q.popleft()
#         cheeze[r][c] = 0
#
#         for k in range(4):
#             nr, nc = r + dr[k], c + dc[k]
#
#             if 0 <= nr < H and 0 <= nc < W:
#                 if cheeze[nr][nc] == 1 and not melt_day[nr][nc]:
#                     melt_day[nr][nc] = melt_day[r][c] + 1
#                     # cnt += 1
#                     Q.append((nr, nc))
#         cnt += 1
#
#

def bfs():
    Q = deque()
    Q.append((0, 0))
    visit[0][0] = 1
    cnt = 0
    while Q:
        r, c = Q.popleft()

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]

            if 0 <= nr < H and 0 <= nc < W:
                if not visit[nr][nc]:
                    if cheeze[nr][nc] == 0:
                        visit[nr][nc] = 1
                        Q.append((nr, nc))
                    if cheeze[nr][nc] == 1:
                        cheeze[nr][nc] += 1
                        cnt += 1
                        visit[nr][nc] = 1
    cnt_lst.append(cnt)
    return cnt





H, W = map(int, input().split())
cheeze = [list(map(int, input().split())) for _ in range(H)]
Q = deque()
cnt_lst = []
time = 0
while 1:
    time += 1
    visit = [[0] * W for _ in range(H)]
    cnt = bfs()
    if cnt == 0:
        break
print(time-1)
print(cnt_lst[-2])
# cnt = 0
# for i in range(W):
#     Q.append((0, i))
#     Q.append((H-1, i))
# for i in range(H):
#     Q.append((i, 0))
#     Q.append((i, W-1))
#
# print(Q)
# first_melt_cheeze()
# print(cheeze)
# print(Q)
# melt_day = [[0] * W for _ in range(H)]
# for r in range(H):
#     for c in range(W):
#         if cheeze[r][c] == 'c':
#             melt_day[r][c] = 1
#             Q.append((r, c))
#
# melt_cheeze()
# print(cheeze)
# print(cnt)
# print(melt_cheeze())
# print(melt_day)

