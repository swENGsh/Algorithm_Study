import sys
sys.stdin = open('2178.txt')

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def find_maze(start,end,count):
    q = deque()
    q.append((start,end,count))
    while q:
        r, c , cnt = q.popleft()
        visit[r][c] == 1
        if r == GR and c == GC:
            print(cnt)
            return
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 < nr <= GR and 0 < nc <= GC and maze[nr][nc] == 1 and visit[nr][nc] == 0:
                q.append((nr,nc,cnt+1))
                visit[nr][nc] = 1
                nr += dr[d]
                nc += dc[d]

    return


GR, GC = map(int, input().split())

maze = [[0]*(GC+1)] + [[0]+list(map(int,input())) for _ in range(GR)]
visit = [[0]*(GC+1) for _ in range(GR+1)]
find_maze(1,1,1)

# #2
# from collections import deque
#
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# def find_maze(start,end):
#     q = deque()
#     q.append((start,end))
#     while q:
#         r, c = q.popleft()
#         visit[r][c] == 1
#         if r == GR and c == GC:
#             print(visit[r][c]+1)
#             return
#         for d in range(4):
#             nr, nc = r + dr[d], c + dc[d]
#             # print('for문 nr,nc',nr,nc)
#             if 0 < nr <= GR and 0 < nc <= GC and maze[nr][nc] == 1 and visit[nr][nc] == 0:
#                 q.append((nr,nc))
#                 visit[nr][nc] = visit[r][c] + 1
#                 nr += dr[d]
#                 nc += dc[d]
#     return
#
#
# GR, GC = map(int, input().split())
#
# maze = [[0]*(GC+1)] + [[0]+list(map(int,input())) for _ in range(GR)]
# visit = [[0]*(GC+1) for _ in range(GR+1)]
# find_maze(1,1)