import sys; sys.setrecursionlimit(10000)

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
def dfs(r, c, cnt):
    if len(cnt) == 6:
        if cnt not in result:
            result.append(cnt)
        return

    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < 5 and 0 <= nc < 5:
            dfs(nr, nc, cnt + data[nr][nc])
data = [list(map(str, input().split())) for _ in range(5)]

result = []
for r in range(5):
    for c in range(5):
        dfs(r, c, data[r][c])
print(len(result))


#==============================================================
# 참고용 -> set사용 코드
# import sys
# input = sys.stdin.readline
#
# dx, dy = [-1,1,0,0], [0,0,-1,1]
# def DFS(x, y, cnt, string):
#     global result
#     string += str(graph[x][y])
#     cnt += 1
#     if cnt == 6:
#         result.add(string)
#         return
#
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         if 0 <= nx < 5 and 0 <= ny < 5:
#             DFS(nx, ny, cnt, string)
#
# graph = [list(map(int, input().split())) for _ in range(5)]
#
# result = set()
# for i in range(5):
#     for j in range(5):
#         DFS(i, j, 0, '')
#
# print(len(result))